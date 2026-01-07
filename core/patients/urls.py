from django.urls import path
from .views import PatientDoctorCreateView, PatientDoctorListView

urlpatterns = [
    path('assign/', PatientDoctorCreateView.as_view()),
    path('patient/<int:patient_id>/', PatientDoctorListView.as_view()),
]
