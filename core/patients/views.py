from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .models import Patient, PatientDoctor
from .serializers import PatientSerializer, PatientDoctorSerializer


# Patient CRUD
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Assign doctor to patient
class PatientDoctorCreateView(generics.CreateAPIView):
    queryset = PatientDoctor.objects.all()
    serializer_class = PatientDoctorSerializer
    permission_classes = [IsAuthenticated]


# List doctors for a patient
class PatientDoctorListView(generics.ListAPIView):
    serializer_class = PatientDoctorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs.get('patient_id')
        return PatientDoctor.objects.filter(patient_id=patient_id)
