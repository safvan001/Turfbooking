from django.urls import path
from .views import *

urlpatterns = [
    path('initiate-otp/', InitiateOtp.as_view()),
    path('verify-otp/', VerifyOtp.as_view()),
]
