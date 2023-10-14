from rest_framework import viewsets
from django.shortcuts import render
from .serializer import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    print('------0000')
    serializer_class=MyTokenObtainPairSerializer

# @api_view(['POST'])
# def Mytoken(reqyest):
#     mytoken={'toke':'fayzulloh'}

#     return Response(data=mytoken)

