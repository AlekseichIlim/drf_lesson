from http.client import responses

from rest_framework import response, status
from rest_framework.test import APITestCase


class TestVehicle(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_car(self):
        data = {
            'title': 'Toyota',
            'descriptions': 'Camry',
        }
        self.client.post(
            '/cars/',
            data=data
        )
        self.assertEqual(response.status, status.HTTP_201_CREATED)
        print(response)


