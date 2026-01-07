from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from patients.views import PatientViewSet
from doctors.views import DoctorViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet)
router.register('doctors', DoctorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),              # ✅ admin ONLY here
    path('api/auth/', include('accounts.urls')),  # auth
    path('api/patients/', include('patients.urls')),
    path('api/', include(router.urls)),
]
