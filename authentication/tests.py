from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from authentication.models import UserManager, USER


class TestHello(TestCase):
    def setUp(self):
        email = "d@gmail.com"
        password = "abc"
        self.user = USER.objects.create_user(email=email, password=password) # TODO: create variable
        self.user.save()

    def test_hello_view(self):
        email = "d@gmail.com"
        password = "abc"
        resp = self.client.post(reverse('login'), data={'username': email, 'password': password})
        self.assertEqual(resp.status_code, 302)
        # self.assertIn(self.article.title, resp.content.decode('utf8'))

