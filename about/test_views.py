from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import AddpostForm

# Create your tests here.
class TestAboutView(TestCase):


    def setUp(self):
        """Creates about me content"""
        self.about_content = About(
            title="About Me", content="This is about me.")
        self.about_content.save()

    def test_render_share_page_with_addpostform(self):
        """Verifies get request for share post via addpostform"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(
            response.context['addpost_form'], AddpostForm)

    def test_successful_addpost_request_submission(self):
        """Test for a user requesting to post on website"""
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Post request received! I endeavour to respond within 2 working days.', response.content)