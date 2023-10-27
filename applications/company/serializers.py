from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from applications.company.models import Company, CompanyProduct
from applications.company.models import Contacts, Location
from applications.product.serializers import ProductSerializer


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('country', 'city', 'street', 'home')


class ContactsSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Contacts
        fields = ('email', 'location')


class CreateCompanySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    contacts = ContactsSerializer()

    class Meta:
        model = Company
        fields = ('category', 'name', 'contacts', 'supplier')


class GetCompanySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    contacts = ContactsSerializer()

    class Meta:
        model = Company
        fields = ('id', 'name', 'category', 'contacts', 'supplier', 'debt')


class CreateCompanyProductSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CompanyProduct
        fields = ('count', 'product', 'company')
