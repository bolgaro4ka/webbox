from django.test import Client, override_settings
import unittest



class SimpleUrlTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.urls = [
                            '',
                            'money/1/',
                            'l/',
                            'reg/',
                            'a/',
                            'a/1/',
                            'u/'
                        ]

    def tg_test(self):
        response = self.client.get(self.urls[0])
        self.assertEqual(response.status_code, 200)
