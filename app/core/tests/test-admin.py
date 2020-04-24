from django.test import TestCase, Client
from django.congtrib.auth import get_user_model
# Generate URLs for Admin page
from django.urls import reverse

class AdminSiteTests(TestCase):

    # Setup function runs before every test TestCase
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@adventureappdev.com',
            password= 'password123'

        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'test@adventureappdev.com',
            password= 'password123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        # respond
        res = self.client.get(url)
        # additional checks that https responds and check actual contains of the
        # feature
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
