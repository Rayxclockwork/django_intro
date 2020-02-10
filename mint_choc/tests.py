from django.test import TestCase
from django.urls import reverse

# Create your tests here.
def test_about_page_status(self):
	url = reverse('about')
	response = self.client.get(url)
	self.assertEqual(response.status_code, 200)

def test_about_templates(self):
	url = reverse('about')
	response = self.client.get(url)
	self.assertTemplateUsed(response, 'about.html'),
	self.assertTemplateUsed(response, 'base.html')
