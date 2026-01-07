from django.contrib import admin
from .models import Patient, PatientDoctor

admin.site.register(Patient)
admin.site.register(PatientDoctor)
