from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import BaseModel

class User(AbstractUser,BaseModel):
    ROLE_CHOICES=(
        ('User','User'),
        ('Owner','Owner'),
        ('Admin','Admin')
    )
    role = models.CharField(max_length=15,choices=ROLE_CHOICES)
    phone_number = models.BigIntegerField()
    REQUIRED_FIELDS = []

    def save(self):
        
        self.set_password(self.password)
        super().save()

    def __str__(self):
        return str(self.username)
    







