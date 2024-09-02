from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Basemodel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract=True

class User_data(AbstractUser,Basemodel):
    ROLE_CHOICES=(
        ('User','User'),
        ('Owner','Owner'),
        ('Admin','Admin')
    )
    role=models.CharField(max_length=15,choices=ROLE_CHOICES)
    REQUIRED_FIELDS = []

    def save(self):
        self.set_password(self.password)
        super().save()

    def __str__(self):
        return str(self.username)
    







