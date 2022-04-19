from django.test import TestCase

from launio.club.forms import CreateContactForm


class TestContactForm(TestCase):
    def test_contact_view_successful(self):
        subject = 'Sended from web La Unio contact form'
        body = {
            'first_name': 'Someone',
            'email_address': 'some@some.com',
            'message': 'Hello',
        }
        message = "\n".join(body.values())
        form = CreateContactForm(body)
        self.assertTrue(form.is_valid())
