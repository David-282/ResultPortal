from tokenize import TokenError

from django.contrib.auth.forms import logger
from django.db import transaction
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import  AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from core.models import User, Department
from .models import Student, Staff
from .serillizers import StudentEnrollmentSerializer, StaffEnrollmentSerializer, CustomTokenObtainSerializer


# Create your views here.


class StudentEnrollment (APIView):
    permission_classes = [AllowAny]
    def post (self,request,*args,**kwargs):
        serializer = StudentEnrollmentSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)

        department_code = serializer.validated_data['department']
        department =  Department.objects.get(department_code=department_code)


        with transaction.atomic():
            user = User()
            user.email = serializer.validated_data['email']
            user.username = serializer.validated_data['username']
            user.first_name = serializer.validated_data['first_name']
            user.last_name = serializer.validated_data['last_name']
            user.set_password(serializer.validated_data['password'])
            user.save()


            student = Student.objects.create(
                user = user,
                department = department,
                entry_year = serializer.validated_data['entry_year'],
            )
            user.save()
            student.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)


class StaffEnrollment(APIView):
    def post(self,request,*args,**kwargs):
        serializer = StaffEnrollmentSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)

        department_code = serializer.validated_data['department']
        department = Department.objects.get(department_code=department_code)

        with transaction.atomic():

            user = User()
            user.email = serializer.validated_data['email']
            user.username = serializer.validated_data['username']
            user.first_name = serializer.validated_data['first_name']
            user.last_name = serializer.validated_data['last_name']
            user.set_password(serializer.validated_data['password'])
            user.role = "staff"
            user.is_staff = True

            user.save()

            staff = Staff.objects.create(
                user = user,
                department = department,
                designation = serializer.validated_data['designation']
            )

            user.save()
            staff.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainSerializer

    def post(self, request, *args, **kwargs):
        user_email = request.data.get("email")
        logger.info(f"User{request.user.get("email")} is attempting to login")

        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            logger.info(f"Invalid token: {e}")
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error({f"An error occurred while login for:{e}"})
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        logger.info(f"User {user_email} has logged in successfully")
        return Response(status=status.HTTP_401_UNAUTHORIZED)
