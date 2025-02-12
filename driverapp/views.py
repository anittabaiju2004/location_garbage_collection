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
