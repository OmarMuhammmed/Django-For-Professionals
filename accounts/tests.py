from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignupPageView

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='test',
            email='test@user.com',
            password='testuser1801'
        )

        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'test@user.com')
        self.assertTrue(user.is_active, True)
        self.assertFalse(user.is_staff, False)
        self.assertFalse(user.is_superuser, False)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='testadmin1801'
        )

        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'admin@test.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.res = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.res.status_code, 200)
        self.assertTemplateUsed(self.res, 'registration/signup.html')
        self.assertContains(self.res, 'Sign Up')
        self.assertNotContains(
            self.res, 'Hi there! I should not be on the page.'
        )

    def test_signup_form(self):
        form = self.res.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.res, 'csrfmiddlewaretoken')

    def test_signup_view(self): # new
        view = resolve('/accounts/signup/')
        self.assertEqual(
        view.func.__name__,
        SignupPageView.as_view().__name__
        )    