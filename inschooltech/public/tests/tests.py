import pytest
from public.models import Test
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from django.urls import reverse


class LabTestTest(APITestCase):

    def setUp(self):
        self.user = User.create_user(
            username='testuser',
            email='testuser@mail.com',
            password='XYLOPHONE'
        )
        self.client.force_authenticate(user=self.user)

    def test_get_tests_authorized(self):
        url = reverse('test-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_OK)
        pass
