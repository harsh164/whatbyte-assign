from django.contrib import admin
from .models import Patient, PatientDoctor


class PatientDoctorInline(admin.TabularInline):
    model = PatientDoctor
    extra = 0


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "age",
    )
    search_fields = (
        "name",
    )
    inlines = [PatientDoctorInline]


@admin.register(PatientDoctor)
class PatientDoctorAdmin(admin.ModelAdmin):
    list_display = (
        "patient",
        "doctor",
    )
