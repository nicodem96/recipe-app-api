'''
Tests for models.
'''
from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):

    def test_create_user(self):

        email = 'test@example.com'
        password = 'testpass123'
        username= "test"
        User = get_user_model()
        user = User.objects.create_user(
        username=username, email=email, password=password
        )
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_email = 'test1@EXAMPLE.com'
        expected_email = 'test1@example.com'
        user = get_user_model().objects.create_user(email = sample_email)
        self.assertEqual(user.email, expected_email)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', username = 'test123')
