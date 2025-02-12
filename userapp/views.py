from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import tbl_register
from .serializers import userregisterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
# from your_app.models import tbl_register
# from your_app.serializers import userregisterSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import tbl_register
from .serializers import userregisterSerializer

class user_registerViewSet(ModelViewSet):
    queryset = tbl_register.objects.all()
    serializer_class = userregisterSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "Registration successful",
                    "role": "user",
                    "name": user.name,
                    "email": user.email,
                    "place": user.place,
                    "address": user.address,
                    "phone": user.phone,
                    
                },
                status=status.HTTP_201_CREATED
            )

        # Extract error messages
        error_messages = {field: errors[0] for field, errors in serializer.errors.items()}

        return Response(
            {"message": "Registration failed", "errors": error_messages},
            status=status.HTTP_400_BAD_REQUEST
        )



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import tbl_register

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import tbl_register

class LoginView(APIView):
    def post(self, request):
        # Retrieve email, phone, and password from the request data
        email = request.data.get('email')
        phone = request.data.get('phone')
        pswd = request.data.get('pswd')
        print(request.data)
        # Ensure either email or phone is provided, along with the password
        if not (email or phone) or not pswd:
            return Response(
                {"error": "Email or phone and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            # Fetch user by email or phone
            if email:  # Login with email
                user = tbl_register.objects.get(email=email)
            elif phone:  # Login with phone
                user = tbl_register.objects.get(phone=phone)

            # Check if the password matches
            if user.pswd == pswd:  # Direct comparison; use hashing in production
                return Response(
                    {"message": "Login successful", "user": user.name,"role":"user"},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "Invalid email/phone or password."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except tbl_register.DoesNotExist:
            # Return the same error if the user doesn't exist
            return Response(
                {"error": "Invalid email/phone or password."},
                status=status.HTTP_400_BAD_REQUEST,
            )

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import ComplaintRegister
from .serializers import ComplaintRegisterSerializer
from django.shortcuts import get_object_or_404

class MyComplaintsView(APIView):
    def get(self, request, user_id):
        complaints = ComplaintRegister.objects.filter(user_id=user_id).order_by('-date')
        serializer = ComplaintRegisterSerializer(complaints, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework import viewsets
from .models import ComplaintRegister
from .serializers import ComplaintRegisterSerializer

class ComplaintRegisterViewSet(viewsets.ModelViewSet):
    queryset = ComplaintRegister.objects.all().order_by('-date')
    serializer_class = ComplaintRegisterSerializer

    def perform_create(self, serializer):
        serializer.save()
