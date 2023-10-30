from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from applications.companies.models import Company, CompanyProduct, Address
from applications.products.serializers import ProductSerializer


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('country', 'city', 'street', 'house')


class CreateCompanySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Company
        fields = ('category', 'name', 'address', 'supplier')


class GetCompanySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Company
        fields = ('id', 'name', 'category', 'address', 'supplier', 'debt')


class CreateCompanyProductSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CompanyProduct
        fields = ('count', 'product', 'company')
