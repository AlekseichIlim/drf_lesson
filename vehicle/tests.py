from http.client import responses

from rest_framework import response, status
from rest_framework.test import APITestCase

from vehicle.models import Car


class TestVehicle(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_car(self):
        data = {
            'title': 'Toyota',
            'descriptions': 'Camry',
        }

        response = self.client.post(
            '/cars/',
            data=data
        )
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {'id': 1, 'milage': [], 'title': 'Toyota', 'descriptions': 'Camry', 'owner': None})

        self.assertTrue(Car.objects.all().exists())

    def test_list_car(self):
        'вывод списка'
        Car.objects.create(title='Toyota1', descriptions='Camry')

        response = self.client.get(
            '/cars/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json(), [{'id': 2, 'milage': [], 'title': 'Toyota1', 'descriptions': 'Camry', 'owner': None}])





