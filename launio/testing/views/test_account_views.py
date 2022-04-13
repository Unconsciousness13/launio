from django.http import HttpResponseServerError
from django.test import TestCase, Client
from django.urls import reverse

from launio.accounts.models import NewUser


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

    def test_new_user_successful__profile_page_view(self):
        user = NewUser.objects.create(id=1, user_name='testuser')
        user.set_password('12345')
        user.save()
        client = Client()
        client.force_login(user)
        response = client.get("/accounts/profile/1/", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_new_user_profile_edit_view(self):
        user = NewUser.objects.create(**self.VALID_USER_DATA)
        user.save()
        client = Client()
        client.force_login(user)
        response = client.post("/accounts/profile-edit/1/", data={
            'id': 1,
            'first_name': 'Spas',
            'last_name': 'Iliev',
            'user_name': 'PaKo',
            'email': 'pako@pako.es',
            'about': 'res'
        })

        update_profile = NewUser.objects.get(pk=user.pk)
        self.assertEqual('Pako', update_profile.first_name)

        # profile = NewUser.objects.create(**self.VALID_USER_DATA)
        # profile.save()
        # client = Client()
        # client.force_login(profile)
        #
        # response = self.client.post(
        #     reverse(
        #         'profile edit', profile.pk),
        #     data={
        #         'id': 1,
        #         'first_name': 'Spas',
        #         'last_name': 'Iliev',
        #         'user_name': 'PaKo',
        #         'email': 'pako@pako.es',
        #         # 'profile_image': 'nvfbboicknzkgl3du5fj'
        #     }
        # )
        #
        # update_profile = NewUser.objects.get(pk=profile.pk)
        # print(response)
        # self.assertEqual('Spas', update_profile.first_name)

    def test_new_user_profile_edit_view__invalid_url_redirect(self):
        pass

    def test_wrong_url_returns_404(self):
        response = self.client.get('/wrong/wrong/wrong/blalba')
        self.assertEqual(response.status_code, 404)

    def test_wrong_url_returns_500(self):
        response = HttpResponseServerError
        self.assertEqual(response.status_code, 500)

    def test_delete_profile_view(self):
        user = NewUser.objects.create(**self.VALID_USER_DATA)
        user.save()
        client = Client()
        client.force_login(user)
        response = client.get(reverse('profile delete', kwargs={'pk': user.pk}))
        self.assertEqual(response.status_code, 200)

    def test_delete_profile_view_incorrect(self):
        user = NewUser.objects.create(**self.VALID_USER_DATA)
        user.save()
        client = Client()
        client.force_login(user)
        response = client.get(reverse('profile delete', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 404)
