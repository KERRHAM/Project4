from django.test import TestCase
from .forms import AddpostForm


class Testaddpostfrom(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = AddpostForm ({
            'name': '.',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")