from django.db import models
from django.contrib.auth.models import AbstractUser

class Basemodel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class User_data(AbstractUser):
    ROLE_CHOICES=(
        ('User','User'),
        ('Owner','Owner'),
        ('Admin','Admin')
    )
    role=models.CharField(max_length=15,choices=ROLE_CHOICES)
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.username)
    







