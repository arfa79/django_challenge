from django.contrib import admin
from .models import PersonalInfo, InsuranceInfo

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'firstname', 'lastname', 'age', 'gender', 'mobile')
    search_fields = ('firstname', 'lastname', 'mobile')
    list_filter = ('gender',)
    ordering = ('lastname',)

@admin.register(InsuranceInfo)
class InsuranceInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'policy_number', 'insurance_value')
    search_fields = ('policy_number', 'car')
    list_filter = ('car',)
    ordering = ('policy_number',)
