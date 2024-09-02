from django.urls import path
from .views import *

urlpatterns = [
    path('initiate-otp/', InitiateOtp.as_view()),
]
