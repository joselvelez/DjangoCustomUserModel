from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):

    def test_new_superuser(self):

        db = get_user_model()

        super_user = db.objects.create_superuser(
            'testuser@test.com', 'username', 'password'
        )
        self.assertEqual(super_user.email, 'testuser@test.com')
        self.assertEqual(super_user.user_name, 'username')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_admin)
        self.assertEqual(str(super_user), 'username')

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@test.com', user_name='testuser', password='password', is_superuser=False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@test.com', user_name='testuser', password='password', is_staff=False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='', user_name='testuser', password='password', is_staff=True
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@test.com', user_name='', password='password', is_staff=True
            )

    def test_new_user(self):
        
        db = get_user_model()

        user = db.objects.create_user(
            'testuser@test.com', 'username', 'password'
        )

        self.assertEqual(user.email, 'testuser@test.com')
        self.assertEqual(user.user_name, 'username')
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='', user_name='testuser', password='password'
            )

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='testuser@test.com', user_name='', password='password'
            )

        