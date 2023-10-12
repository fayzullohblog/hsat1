from rest_framework import serializers
from rest_framework import viewsets
from .models import MyUser

class MyUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=MyUser()
        fields='__all__'

        