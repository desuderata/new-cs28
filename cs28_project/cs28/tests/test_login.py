from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class LoginTest(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(username='testuser',
                                                        first_name='Test',
                                                        last_name='User',
                                                        email='test@test.com')
        self.user.set_password('password')
        self.user.save()
        self.assertTrue(created, "User was not created.")

    def test_login(self):
        response = self.client.post(reverse('cs28:login'),
                                    {'username': 'testuser',
                                     'password': 'password'})
        self.assertEqual(self.user.id,
                         int(self.client.session['_auth_user_id']),
                         "Login failed. "
                         "Perhaps a different user was logged in?")
        self.assertEqual(response.url, reverse('cs28:index'),
                         "User was not redirected to home page after login")
