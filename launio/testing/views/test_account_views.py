from django.test import TestCase

from launio.accounts.models import NewUser


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        NewUser.objects.create(first_name='Spas', last_name='Spasov', user_name='Spase', email='spas@spas.es')

    # def test_first_name(self):
    #     user = NewUser.objects.get(id=1)
    #     field_label = user._meta.get_field('first_name').verbose_name
    #     self.assertEqual(field_label, 'first name')

    # def test_get_absolute_url(self):
    #     user = NewUser.objects.get(id=1)
    #
    #     self.assertEqual(user.get_success_url(), '/accounts/profile/1/')
