# from django.test import TestCase
# from django.urls import reverse
# # Create your tests here.
# from authentication.models import UserManager, USER
#
#
# class TestHello(TestCase):
#     def setUp(self):
#         user = UserManager.create_user(self, email="d@gmail.com")
#         # user = self.model(email=email)
#         user.set_password(password)
#         user.save()
#         # email.save()
#         # password = UserManager(name="d@gmail.com")
#         # password.save()
#
#     def test_hello_view(self):
#         resp = self.client.get(reverse('authentication'))
#         self.assertEqual(resp.status_code, 200)
#         self.assertIn(self.article.title, resp.content.decode('utf8'))
#
