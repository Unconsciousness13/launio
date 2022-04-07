# from django.contrib.auth import get_user_model
# from django.test import TestCase
#
# from launio.accounts.models import NewUser
#
#
# class UserAccountTest(TestCase):
#
#     def test_new_superuser(self):
#         db = NewUser
#         super_user = db.objects.create_superuser(
#             'testuser@gmail.com', 'username', 'firstname', 'lastname', 'password'
#         )
#         print(super_user)
#         self.assertEqual(super_user.email, 'testuser@gmail.com')
#         self.assertEqual(super_user.first_name, 'firstname')
#         self.assertEqual(super_user.last_name, 'lastname')
#         self.assertEqual(super_user.user_name, 'username')
#         self.assertTrue(super_user.is_superuser)
#         self.assertTrue(super_user.is_staff)
#         self.assertTrue(super_user.is_active)
#         self.assertEqual(str(super_user), "username")
#
#         with self.assertRaises(ValueError):
#             db.objects.create_superuser(
#                 email='testuser@gmail.com', user_name='username1', first_name='Pako', last_name='Iliev',
#                 password='password',
#                 is_superuser=False
#             )
#
#         with self.assertRaises(ValueError):
#             db.objects.create_superuser(
#                 email='testuser@gmail.com', user_name='username1', first_name='Pako', last_name='Iliev',
#                 password='password',
#                 is_staff=False
#             )
#
#         with self.assertRaises(ValueError):
#             db.objects.create_superuser(
#                 email='', user_name='username1', first_name='Pako', last_name='Iliev', password='2password282',
#                 is_superuser=True
#             )
#
#     def test_new_user(self):
#         db = get_user_model()
#         user = db.objects.create_user(
#             'email', 'username', 'firstname', 'lastname', 'password'
#         )
#         self.assertEqual(user.email, 'testuser@gmail.com')
#         self.assertEqual(user.user_name, 'Pako')
#         self.assertEqual(user.first_name, 'Pako')
#         self.assertEqual(user.last_name, 'Iliev')
#         self.assertFalse(user.is_superuser)
#         self.assertFalse(user.is_staff)
#         self.assertTrue(user.is_active)
#
#         with self.assertRaises(ValueError):
#             db.objects.create_user(
#                 email='', user_name='Pako', first_name='Plamen', last_name='Iliev', password='2password282'
#             )