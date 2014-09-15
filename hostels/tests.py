from django.test import TestCase
from django.test.client import Client
from django.test.utils import override_settings

class HomePageTest(TestCase):
	def test_home_page(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		#self.assertTrue('' in response.context)


class InfoPageTest(TestCase):
	def test_info_page(self):
		response = self.client.get('/info/')
		self.assertEqual(response.status_code, 200)

