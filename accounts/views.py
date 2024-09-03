from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.conf import settings
from accounts.serializers import *
import requests

class UserRegistrationView(generics.ListCreateAPIView):
    "This view handle User Registration"
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserLoginView(APIView):
    "This view handle User login"

    def post(self,request):
        serializers=UserLoginSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        user=serializers.validated_data['user']

        refresh=RefreshToken.for_user(user)
        return Response({
            'access':str(refresh.access_token),
            'refrseh':str(refresh),
            'message':'User authenticated Successfully'
        },status=status.HTTP_200_OK)
    

class InitiateOtp(APIView):
    def get(self,request, *args, **kwargs):
        phone_number = request.GET.get("phone_number",'')
        print(phone_number)
        if User.objects.filter(phone_number=phone_number).exists():
            url = settings.TWO_FACTOR_BASE_URL
            api_key = settings.TWO_FACTOR_API_KEY
            response = requests.get('${url}${api_key}SMS/+91${phone_number}/AUTOGEN/OTP1')
            return Response(response.text)
        else:
            return Response('user not found')