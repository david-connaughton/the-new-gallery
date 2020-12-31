from django.test import TestCase


class TestProfiles(TestCase):

    def test_profile_no_user(self):
        response = self.client.get('/profile/user/')
        self.assertNotEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'profiles/profile.html')
