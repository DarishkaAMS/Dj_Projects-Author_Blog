from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from authentication.models import UserManager, USER


class TestHello(TestCase):
    def setUp(self):
        self.user = UserManager.create_user(self, email="d@gmail.com", password="abc") #!!!!!!!
        self.user.save()

    def test_hello_view(self):
        resp = self.client.get(reverse('authentication'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.article.title, resp.content.decode('utf8'))

