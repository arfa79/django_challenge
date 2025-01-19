# from django.test import TestCase


from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import PersonalInfo, InsuranceInfo

class ProjectTests(APITestCase):
    def setUp(self):
        # ایجاد کاربر و دریافت توکن
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")
        response = self.client.post("/api/token/", {"username": "testuser", "password": "password123"})
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        # ایجاد داده‌های اولیه برای PersonalInfo
        self.personal_info = PersonalInfo.objects.create(
            user=self.user,
            firstname="Ali",
            lastname="Hosseini",
            age=30,
            gender="Male",
            mobile="123456789"
        )

        # ایجاد داده‌های اولیه برای InsuranceInfo
        self.insurance_info = InsuranceInfo.objects.create(
            user=self.personal_info,
            car="Toyota Corolla",
            policy_number="ABC123",
            insurance_value=1500.00
        )

    def test_permission_required_for_crud(self):
        """
        اطمینان از اینکه عملیات CRUD بدون توکن قابل انجام نیست.
        """
        self.client.credentials()  # حذف توکن
        response = self.client.get(f"/api/personal-info/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.post("/api/personal-info/", {
            "user": self.user.id,
            "firstname": "Reza",
            "lastname": "Ahmadi",
            "age": 25,
            "gender": "Male",
            "mobile": "987654321"
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_insurance_info_serializer_excludes_policy_number(self):
        """
        اطمینان از اینکه در سریالایزر InsuranceInfo، مقدار فیلد policy_number برگشت داده نمی‌شود.
        """
        response = self.client.get(f"/api/insurance-info/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # چک کردن اینکه فیلد policy_number وجود ندارد
        for insurance in response.data:
            self.assertNotIn("policy_number", insurance)


