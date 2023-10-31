from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from applications.authentication.models import User
from applications.companies.models import Address, Company
from applications.products.models import Product


class CompanyApiTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser', email='test@mail.com', password='testpassword')
        cls.address = Address.objects.create(
            country='BY', city='test2', street='test3', house='4')
        cls.product = Product.objects.create(
            name='testname', model='testmodel', launch_date='2023-03-10')

    def setUp(self):
        self.client.login(username='testuser', password='testpassword')

    def test_create_company(self):
        address = {'country': 'BY', 'city': 'test2',
                   'street': 'test3', 'house': '4'}
        url = reverse('companies-list')
        data = {'name': 'test1', 'email': 'test1@mail.com', 'address': address}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['address'], address)

    def test_search_company_by_id(self):
        self.company = Company.objects.create(
            owner=self.user, name='test1', email='test1@mail.com', address=self.address)
        url = reverse('companies-detail', kwargs={'pk': self.company.pk})

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.company.id)
        self.assertEqual(response.data['name'], self.company.name)
        self.assertEqual(response.data['email'], self.company.email)
        self.assertEqual(response.data['address']
                         ['country'], self.address.country)
        self.assertEqual(response.data['address']['city'], self.address.city)
        self.assertEqual(response.data['address']
                         ['street'], self.address.street)
        self.assertEqual(response.data['address']['house'], self.address.house)

    def test_create_product(self):
        self.company = Company.objects.create(
            owner=self.user, name='test1', email='test1@mail.com', address=self.address)
        url = reverse('products-list', kwargs={'company_id': self.company.pk})
        data = {'count': 1, 'product': self.product.pk, }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['count'], data['count'])
        self.assertEqual(response.data['product'], self.product.pk)

    def test_create_employee(self):
        self.company = Company.objects.create(
            owner=self.user, name='test1', email='test1@mail.com', address=self.address)
        url = reverse('employees-list', kwargs={'company_id': self.company.pk})
        data = {'first_name': 'testname',
                'last_name': 'test', 'email': 'email@mail.com'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'], data['first_name'])
        self.assertEqual(response.data['last_name'], data['last_name'])
