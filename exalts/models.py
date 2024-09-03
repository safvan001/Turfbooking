from django.db import models
from accounts.models import User

class Rate(models.Model):
    TYPES=(
        ('11s','11s'),
        ('7s','7s'),
        ('5s','5s')
        ('Cricket','Cricket'),
        ('Tennis','Tennis'),
        ('Basketball','Basketball'),
        ('TableTennis','TableTennis'),
        ('Volleyball','Volleyball'),
        ('Badminton','Badminton'),
        ('Swimming Pool','Swimming Pool')
    )
    types=models.CharField(max_length=20,choices=TYPES)
    price=models.IntegerField()

    def __str__(self):
        return f"{self.types} - {self.price}"


class Turf(models.Model):
    name=models.CharField()
    logo=models.ImageField(upload_to='logo')
    turf_image_1=models.ImageField(upload_to='turfimages')
    turf_image_2=models.ImageField(upload_to='turfimages')
    turf_images_3=models.ImageField(upload_to='turfimages')
    price=models.ManyToManyField(Rate)
    is_locker=models.BooleanField(default=False)
    is_parking=models.BooleanField(default=False)
    is_cctv=models.BooleanField(default=False)
    is_washroom=models.BooleanField(default=False)
    is_dressingroom=models.BooleanField(default=False)
    is_purifiedwater=models.BooleanField(default=False)
    is_firstaidkit=models.BooleanField(default=False)

    def __str__(self):
        return self.name



    

# Create your models here.
