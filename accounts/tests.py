from django.test import TestCase
from django.contrib.auth import get_user_model 
from django.urls import reverse

class UserTests(TestCase):
    def test_create_user(self):
        User=get_user_model()
        user=User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass1234",
        )
        self.assertEqual(user.username,"testuser")
        self.assertEqual(user.email,"testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser) 
    def test_create_superuser(self):
        User=get_user_model()
        admin_user=User.objects.create_superuser(
            username="testsuperuser",
            email="testsuperuser@example.com",
            password="testpass1234",
        )
        self.assertEqual(admin_user.username,"testsuperuser")
        self.assertEqual(admin_user.email,"testsuperuser@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpPageTests(TestCase):
    def test_url_exists_at_right_location(self):
        response=self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code,200)
    
    def test_signup_viewname(self):
        response=self.client.get(reverse("signup"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"registration/signup.html")
    
    def test_signup_form(self):
        response=self.client.post(
            reverse("signup"),{
                "username":"newuser",
                "email":"newuser@email.com",
                "password1":"newpass123",
                "password2":"newpass123",

            },
        )
        self.assertEqual(response.status_code,302)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username,"newuser")
        self.assertEqual(get_user_model().objects.all()[0].email,"newuser@email.com")




# Create your tests here.
