from django.test import Client, override_settings
from django.test import TestCase


COUNT = 0

urls = {
        '/t/': 200,
        '/t/money/1/': 200,
        '/t/l/': 200,
        '/t/reg/': 200,
        '/t/a/': 302,
        '/t/a/1/': 302,
        }

def test_autogen_factory(url, code):
    global COUNT
    COUNT +=1
    func = f"""
def test_tg_{COUNT-1}_autogen_{code}(self):
    response = self.client.get('{url}')
    self.assertEqual(response.status_code, {code})

"""

    return func

class SimpleUrlTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.login(username="testik", password="abobavirus")
        
        

    for i in urls.keys():
        exec(test_autogen_factory(i, urls[i]))
        # print(test_autogen_factory(i, urls[i]))
