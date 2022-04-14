from django.core.exceptions import ValidationError
from django.test import TestCase

from launio.accounts.models import NewUser


class NewUserTests(TestCase):
    VALID_USER_DATA = {
        'first_name': 'Pako',
        'last_name': 'Iliev',
        'user_name': 'PaKo',
        'email': 'pako@pako.es',
        'id': 1,
    }

    def test_profile_create__when_first_name_contain_only_letters__expect_success(self):
        profile = NewUser(**self.VALID_USER_DATA)
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_create__when_first_name_contain_a_digit__expect_fail(self):
        first_name = 'Pako9'
        profile = NewUser(first_name=first_name,
                          last_name=self.VALID_USER_DATA['last_name'],
                          user_name=self.VALID_USER_DATA['user_name'], )

        with self.assertRaises(ValidationError) as context:
            profile.clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_last_name_contain_a_digit__expect_fail(self):
        last_name = 'Iliev9'
        profile = NewUser(last_name=last_name,
                          first_name=self.VALID_USER_DATA['first_name'],
                          user_name=self.VALID_USER_DATA['user_name'], )

        with self.assertRaises(ValidationError) as context:
            profile.clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_return_correct_user_name__expect_correct(self):
        profile = NewUser(**self.VALID_USER_DATA)
        profile.save()
        self.assertEqual(str(profile.user_name), profile.__str__())

    def test_profile_if_superuser(self):
        profile = NewUser(**self.VALID_USER_DATA)
        profile.is_superuser = True
        profile.clean()
        profile.save()
        self.assertTrue(profile.is_superuser, True)

    def test_profile_if_not_superuser(self):
        profile = NewUser(**self.VALID_USER_DATA)
        profile.is_superuser = False
        profile.save()
        self.assertFalse(profile.is_superuser, False)

    def test_if_user_email_is_correct(self):
        profile = NewUser(**self.VALID_USER_DATA)
        profile.save()
        self.assertEqual(profile.email, 'pako@pako.es')

    def test_username___expect_raise_if_not_letters_or_numbers(self):
        user_name = 'IPaKo_ '
        profile = NewUser(user_name=user_name,
                          first_name=self.VALID_USER_DATA['first_name'],
                          last_name=self.VALID_USER_DATA['user_name'], )

        with self.assertRaises(ValidationError) as context:
            profile.clean()
            profile.save()
        self.assertIsNotNone(context.exception)
