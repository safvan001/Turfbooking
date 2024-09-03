from django.urls import path
from .views import *

urlpatterns = [
    path('user-signup/',UserRegistrationView.as_view(),name='userlogin'),
    path('user-login/',UserLoginView.as_view(),name='usersignup'),
    path('initiate-otp/', InitiateOtp.as_view()),
]
