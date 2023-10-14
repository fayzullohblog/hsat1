from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.tokens import Token



class MyTokenObtainPairSerializer(serializers.TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user) -> Token:
        print('---------------------------1')
        token=super().get_token(user)
        token['username']=user.username
        print('-----2',token)
        
        return token
        



        