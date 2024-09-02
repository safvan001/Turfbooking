from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from django.conf import settings
import requests

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