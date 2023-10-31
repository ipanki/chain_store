from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from applications.authentication.models import User
from applications.companies.models import Address, Company


class CompanyApiTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser', email='test@mail.com', password='testpassword')
        cls.address = Address.objects.create(
            country='BY', city='test2', street='test3', house='4')

    def setUp(self):
        self.client.login(username='testuser', password='testpassword')

    def test_create_company(self):
        address = {'country': 'BY', 'city': 'test2',
                   'street': 'test3', 'house': '4'}
        url = reverse('companies-list')
        data = {'name': 'test1', 'email': 'test1@mail.com', 'address': address}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'test1')
        self.assertEqual(response.data['email'], 'test1@mail.com')
        self.assertEqual(response.data['address'], address)

    def test_search_company_by_id(self):
        self.company = Company.objects.create(
            owner=self.user, name='test1', email='test1@mail.com', address=self.address)
        url = reverse('companies-detail', kwargs={'pk': self.company.pk})

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.company.id)
