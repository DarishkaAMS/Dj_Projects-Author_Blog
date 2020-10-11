from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from authentication.models import UserManager, User
import requests


class TestUser(TestCase):
    def setUp(self):
        email = "d@gmail.com"
        password = "abc"
        username = "HELLO"
        self.user = User.objects.create_user(email=email, password=password, username=username)
        self.user.save()

    def test_user_view(self):
        email = "d@gmail.com"
        password = "abc"
        username = "HELLO"
        resp = self.client.post(reverse('login'), data={'username': email, 'password': password, 'username': username})

        self.assertEqual(resp.status_code, 200)

