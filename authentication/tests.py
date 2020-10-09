from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from authentication.models import UserManager, USER


class TestHello(TestCase):
    def setUp(self):
        self.email = "d@gmail.com"
        self.password = "abc"
        self.user = USER.objects.create_user(email=self.email, password=self.password) # TODO: create variable
        self.user.save()

    def test_hello_view(self):
        resp = self.client.post(reverse('login'), data={'email': self.email, 'password':self.password})
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.article.title, resp.content.decode('utf8'))

