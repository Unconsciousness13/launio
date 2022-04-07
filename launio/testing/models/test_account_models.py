from django.core.exceptions import ValidationError
from django.test import TestCase

from launio.accounts.models import NewUser


class NewUserTests(TestCase):
    VALID_USER_DATA = {
        'first_name': 'Pako',
        'last_name': 'Iliev',
        'user_name': 'PaKo',
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
