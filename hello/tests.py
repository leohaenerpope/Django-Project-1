from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class WebsiteTest(TestCase):
    def test_hello_world_access(self):
        response = self.client.get(reverse('hello_there'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hello/hello_there.html')
        self.assertTemplateNotUsed(response, 'hello/hello_there1.html')