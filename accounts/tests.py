from django.test import TestCase
from django.contrib.auth import get_user_model


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
