from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.tokens import Token



class MyTokenObtainPairSerializer(serializers.TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user) -> Token:
        token=super().get_token(user)
        token['username']=user.username
       
        
        return token
        



        