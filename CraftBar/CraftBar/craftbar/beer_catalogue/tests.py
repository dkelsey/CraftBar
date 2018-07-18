import requests
from rest_framework import status
from rest_framework.test import APITestCase

admin_name = 'admin'
admin_password = 's3cr3t123'

non_employee_name = 'buddy'
non_employee_password = 'buddy123'


class AnonymousUserTests(APITestCase):
    def setUp(self):
        self.new_beer = {
            'name': 'hot-dog-water',
            'brewery': 'the sink',
            'beer_style': 'gross',
            'price': '1.99'
        }
        self.beer_to_delete = {
            'id': '1',
            'name': 'hot-dog-water',
            'brewery': 'the sink',
            'beer_style': 'gross',
            'price': '1.99'
        }

    def tearDown(self):
        pass

    def test_public_user_can_list_beers(self):
        """
        Ensure an unauthenticated user can list beers.
        """
        response = requests.get('http://192.168.101.11:5000/beers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Request for beers failed")
        self.assertTrue(len(response.json()) > 0, "Request returned no beers")

    def test_public_user_can_not_add_beers(self):
        """
        Ensure an unauthenticated user can not add a beers.
        """
        response = requests.post('http://192.168.101.11:5000/beers/', self.new_beer)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, "public user add a new beer request failed")

    def test_public_user_can_not_update_a_beers(self):
        """
        Ensure an unauthenticated user can not update a beers.
        """
        response = requests.put('http://192.168.101.11:5000/beers/', self.beer_to_delete)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, "public user add a new beer request failed")


class NonEmployeesUserTests(APITestCase):
    def setUp(self):
        self.userid = non_employee_name
        self.password = non_employee_password

        self.new_beer = {
            'name': 'hot-dog-water',
            'brewery': 'the sink',
            'beer_style': 'gross',
            'price': '1.99'
        }
        self.beer_to_delete = {
            'id': '1',
            'name': 'hot-dog-water',
            'brewery': 'the sink',
            'beer_style': 'gross',
            'price': '1.99'
        }

    def tearDown(self):
        pass

    def test_non_employee_can_list_beers(self):
        """
        Ensure an authenticated user who is not an employee can list beers.
        """
        response = requests.get('http://%s:%s@192.168.101.11:5000/beers/' % (self.userid, self.password))
        self.assertEqual(response.status_code, status.HTTP_200_OK, "user: %s : Request for beers failed" % self.userid)
        self.assertTrue(len(response.json()) > 0, "Request returned no beers")

    def test_non_employee_can_not_add_beers(self):
        """
        Ensure an unauthenticated user can list beers.
        """
        response = requests.post(
            'http://%s:%s@192.168.101.11:5000/beers/' % (self.userid, self.password),
            self.new_beer)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, "public user add a new beer equest failed")
        self.assertTrue(len(response.json()) > 0, "Request returned no beers")


class EmployeeUserTests(APITestCase):
    def setUp(self):
        self.userid = admin_name
        self.password = admin_password

        self.new_beer = {
            'name': 'hot-dog-water',
            'brewery': 'the sink',
            'beer_style': 'gross',
            'price': '1.99',
            'description': 'tastes like soup'
        }
        self.beer_to_delete = {
            'id': '1',
            'name': 'hot-dog-water',
            'brewery': 'the sink',
            'beer_style': 'gross',
            'price': '1.99'
        }

    def tearDown(self):
        pass

    def test_employee_can_list_beers(self):
        """
        Ensure an employee can list beers.
        """
        response = requests.get('http://%s:%s@192.168.101.11:5000/beers/' % (self.userid, self.password))
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Request for beers failed")
        self.assertTrue(len(response.json()) > 0, "Request returned no beers")

    def test_employee_can_add_a_beer(self):
        """
        Ensure an employee can add a beers.
        """
        response = requests.post('http://%s:%s@192.168.101.11:5000/beers/' % (self.userid, self.password), self.new_beer)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "Employee request to add a beers failed")
        self.assertTrue(len(response.json()) > 0, "Request returned no beers")
