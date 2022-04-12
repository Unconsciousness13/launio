from django.test import TestCase
from django.urls import reverse


class NewUserViewsTests(TestCase):
    VALID_USER_DATA = {
        'first_name': 'Pako',
        'last_name': 'Iliev',
        'user_name': 'PaKo',
        'email': 'pako@pako.es',
        'id': 1,
    }

    def test_new_user_success_login_response_status_code(self):
        self.client.login(**self.VALID_USER_DATA)
        response = self.client.get(reverse('show index'))
        self.assertEqual(response.status_code, 200)

    def test_new_user_login_successful_login(self):
        response = self.client.get(reverse('login page'))

        self.assertTemplateUsed(response, 'profile/login.html')

    # def test_new_user_successful__profile_page_view(self):
    #     user = self.VALID_USER_DATA
    #     print(user)
    #     response = self.client.get(reverse('profile view', user['id']))
    #     self.assertTemplateUsed(response, '/accounts/profile/1/')

    def test_new_user_profile_edit_view(self):
        pass

    def test_new_user_profile_edit_view__invalid_url_redirect(self):
        pass

    def test_wrong_url_returns_404(self):
        response = self.client.get('/something/really/weird/')
        self.assertEqual(response.status_code, 404)
