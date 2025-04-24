from rest_framework import serializers
from .models import PersonalInfo, InsuranceInfo

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'

class InsuranceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceInfo
        fields = 'car', 'policy_number', 'user'
    return fields