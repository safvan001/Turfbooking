from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import BaseModel

class User(AbstractUser,BaseModel):
    username=None
    ROLE_CHOICES=(
        ('User','User'),
        ('Owner','Owner'),
        ('Admin','Admin')
    )
    role = models.CharField(max_length=15,choices=ROLE_CHOICES)
    phone_number = models.BigIntegerField()
    email=models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','role','password']


    def __str__(self):
        return self.email
    







