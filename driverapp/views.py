from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from driverapp.models import DriverRegister
from driverapp.serializers import DriverRegisterSerializer

class DriverRegisterViewSet(viewsets.ModelViewSet):
    queryset = DriverRegister.objects.all().order_by('-id')
    serializer_class = DriverRegisterSerializer
    http_method_names=['post']


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from driverapp.models import DriverRegister

class DriverLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            driver = DriverRegister.objects.get(email=email)

            # Check if the entered password matches the stored password
            if driver.password != password:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the driver is approved
            if driver.status != 'approved':
                return Response({'error': 'Your account is not approved'}, status=status.HTTP_403_FORBIDDEN)

            return Response({'message': 'Login successful', 'driver_id': driver.id, 'name': driver.name,'role':'driver'}, status=status.HTTP_200_OK)

        except DriverRegister.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from userapp.models import ComplaintRegister
from driverapp.models import DriverRegister
from .serializers import ComplaintSerializer

class DriverComplaintListView(APIView):
    def get(self, request, driver_id):
        try:
            driver = DriverRegister.objects.get(id=driver_id)
            complaints = ComplaintRegister.objects.filter(driver=driver)
            serializer = ComplaintSerializer(complaints, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DriverRegister.DoesNotExist:
            return Response({"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)

class UpdateComplaintStatusView(APIView):
    def put(self, request, complaint_id):
        try:
            complaint = ComplaintRegister.objects.get(id=complaint_id)
            if complaint.driver.id != int(request.data.get("driver_id")):
                return Response({"error": "This complaint is not assigned to you"}, status=status.HTTP_400_BAD_REQUEST)

            status_choice = request.data.get("status")
            if status_choice not in ['resolved', 'rejected']:
                return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

            complaint.status = status_choice
            complaint.save()
            return Response({"message": "Status updated successfully"}, status=status.HTTP_200_OK)

        except ComplaintRegister.DoesNotExist:
            return Response({"error": "Complaint not found"}, status=status.HTTP_404_NOT_FOUND)
 