from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=True)
    email=serializers.EmailField(required=False)
    class Meta:
        model=User
        fields=('id','uuid','phone_number','password','first_name','last_name','email','role')
    
    def create(self,validated_data):
        password=validated_data.pop('password')
        user=User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
class UserLoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)

    def validate(self,attrs):
        email=attrs.get('email')
        password=attrs.get('password')
        user=authenticate(email=email,password=password)
        if user is None:
            raise serializers.ValidationError('Invalid Credentials')
        
        attrs['user']=user
        return attrs
    

    