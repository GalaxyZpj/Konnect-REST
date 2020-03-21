from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import date


class UserTests(TestCase):
    def test_create_user(self):
        """Test for creating new users"""
        user = get_user_model().objects.create_user(
            first_name='Admin',
            last_name='Jain',
            gender='male',
            dob=date(2000, 9, 19),
            mobile='9999999999',
            username='galaxyzpj',
            email='test@gmail.com',
            password='Test123@@'
        )
        self.assertEqual(user, get_user_model().objects.get(email='test@gmail.com'))

    def test_create_superuser(self):
        """Test for creating new super users"""
        user = get_user_model().objects.create_superuser(
            username='galaxyzpj',
            email='test@GMAIL.com',
            password='Test123@@'
        )
        self.assertEqual(user, get_user_model().objects.get(email="test@gmail.com"))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_check_normalized_email(self):
        """Test for checking for normalization of email"""
        user = get_user_model().objects.create_user(
            first_name='Admin',
            last_name='Jain',
            gender='male',
            dob=date(2000, 9, 19),
            mobile='9999999999',
            username='galaxyzpj',
            email='test@GMAIL.com',
            password='Test123@@'
        )
        self.assertEqual(user.email, 'TEST@GMAIL.com'.lower())
