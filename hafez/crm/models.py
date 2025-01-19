from django.db import models
from django.contrib.auth.models import User

class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="personal_info")
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class InsuranceInfo(models.Model):
    user = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name="insurance_info")
    car = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=20, unique=True)
    insurance_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.car} - {self.policy_number}"