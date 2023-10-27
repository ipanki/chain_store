from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend

from applications.company.serializers import CreateCompanySerializer, GetCompanySerializer, CreateCompanyProductSerializer
from applications.company.models import Company, CompanyProduct


class CompanyViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateCompanySerializer
    queryset = Company.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ('contacts__location__country',)
    filterset_fields = ('category',)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return GetCompanySerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], url_path='search')
    def get_company_by_product_id(self, request, pk):
        product = CompanyProduct.objects.filter(product__id=pk).values_list('company__id', flat=True)
        company = Company.objects.filter(pk__in=product)
        serializer = GetCompanySerializer(company, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False, methods=['post'], url_path='stats')
    def debt_statistics(self, request):
        avg_debt = Company.objects.aggregate(average_debt=Avg("debt"))
        stats = Company.objects.filter(debt__gt=avg_debt['average_debt'])
        serializer = GetCompanySerializer(stats, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class CompanyProductViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateCompanyProductSerializer
    queryset = CompanyProduct.objects.all()

