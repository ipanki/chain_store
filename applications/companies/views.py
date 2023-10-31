from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from applications.companies.models import Company, CompanyProduct, Employee
from applications.companies.permissions import (CompanyPermission,
                                                CompanyProductPermission)
from applications.companies.serializers import (CreateCompanyProductSerializer,
                                                CreateCompanySerializer,
                                                CreateEmployeeSerializer,
                                                GetCompanySerializer)
from applications.companies.services import generate_qrcode
from applications.companies.tasks import send_by_email


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = (CompanyPermission,)
    serializer_class = CreateCompanySerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ('contacts__location__country',)
    filterset_fields = ('category',)

    def get_queryset(self):
        queryset = Company.objects.filter(owner=self.request.user)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return GetCompanySerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'], url_path='search')
    def get_company_by_product_id(self, request, pk):
        company = self.get_queryset().filter(products__product__id=pk)
        serializer = GetCompanySerializer(company, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False, methods=['post'], url_path='stats')
    def debt_statistics(self, request):
        avg_debt = Company.objects.aggregate(average_debt=Avg("debt"))
        stats = self.get_queryset().filter(debt__gt=avg_debt['average_debt'])
        serializer = GetCompanySerializer(stats, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=True, methods=['post'], url_path='qrcode')
    def get_qrcode(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        qr = generate_qrcode(company.email)
        send_by_email.delay(request.user.email, qr)
        return Response(status=status.HTTP_200_OK, data='QRcode has been sent to your email')


class CompanyProductViewSet(viewsets.ModelViewSet):
    permission_classes = (CompanyProductPermission,)
    serializer_class = CreateCompanyProductSerializer

    def get_queryset(self):
        queryset = CompanyProduct.objects.filter(
            company__owner=self.request.user)
        return queryset


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateEmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.filter(company__owner=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        company = self.request.user.companies.filter(
            pk=request.data['company']).first()
        if company:
            return super().create(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="You can only add employees to your own companies")
