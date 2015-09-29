from rest_framework import status
from rest_framework.test import APITestCase


class ContactDetailViewsTestCase(APITestCase):
    fixtures = ['api_views_testdata.json']

    def test_detail(self):
        # Ensure that existent contact throw a 200.
        resp = self.client.get('/api/notebook/4/')
        self.assertEqual(resp.status_code, 200)
        # Checking get method correct data retuns
        self.assertEqual(resp.data['name'], "Sergey")
        # Ensure put method update "name" field  and throw a 200.
        resp = self.client.put('/api/notebook/4/', {"name": "Vova"})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['name'], "Vova")
        # Not valid data must throw a 400
        resp = self.client.put('/api/notebook/4/', {"test": "Vova"})
        self.assertEqual(resp.status_code, 400)
        # Delete returns 204
        resp = self.client.delete('/api/notebook/4/')
        self.assertEqual(resp.status_code, 204)
        # Ensure that non-existent contact throw a 404.
        resp = self.client.get('/api/notebook/4/')
        self.assertEqual(resp.status_code, 404)


class ContactListViewsTestCase(APITestCase):
    fixtures = ['api_views_testdata.json']

    def test_get_list(self):
        resp = self.client.get('/api/notebook/')
        self.assertEqual(resp.status_code, 200)
