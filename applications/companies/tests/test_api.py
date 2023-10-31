from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from applications.companies.models import Company, CompanyProduct, Address
from applications.authentication.models import User


class CompanyApiTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', email='test@mail.com', password='testpassword')
        cls.address = Address.objects.create(country='BY', city='test2', street='test3', house='4')
        cls.address.save()

    def setUp(self):
        self.client.login(username='testuser', password='testpassword')

    def test_create_company(self):
        url = reverse('companies-list')
        data = {'owner': self.user.pk, 'name': 'test1', 'email': 'test1@mail.com', 'address': self.address.pk}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)

    def test_search_company_by_id(self):
        self.company = Company.objects.create(owner=self.user, name='test1', email='test1@mail.com', address=self.address)
        url = reverse('companies-get-company-by-product-id', kwargs={'pk': self.company.pk})

        response = self.client.post(url, pk=1, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Company.objects.get(pk=self.company.pk), self.company)
