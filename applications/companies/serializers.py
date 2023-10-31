from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from applications.companies.models import (Address, Company, CompanyProduct,
                                           Employee)
from applications.products.serializers import ProductSerializer


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('country', 'city', 'street', 'house')


class CreateCompanySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Company
        fields = ('category', 'name', 'email', 'address', 'supplier')


class GetCompanySerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Company
        fields = ('id', 'name', 'category', 'email',
                  'address', 'supplier', 'debt')


class CreateCompanyProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyProduct
        fields = ('count', 'product', 'company')


class GetCompanyProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CompanyProduct
        fields = ('count', 'product')


class CreateEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'email', 'company')
