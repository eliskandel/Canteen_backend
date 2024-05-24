from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView
)
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer,UserLoginSerializer,UserLogoutSerializer
from rest_framework.authtoken.models import Token
class UserCreateView(CreateAPIView):
    serializer_class=UserSerializer
    
class UserLoginView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        serializer=UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username=serializer.validated_data.get('username')
        password=serializer.validated_data.get('password')
        
        try:
            user=User.objects.get(username=username)
        except:
            return Response({"message":"Invalid Credentials"})
        if not user.check_password(password):
            return Response({"message":"Invalid Credentials"})
        
        token, create=Token.objects.get_or_create(user=user)
        return Response({"message":"Login Successful", "token":token.key})


class UserLogoutView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        serializer=UserLogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_token=serializer.validated_data.get('token')
        try: 
            token=Token.objects.get(key=user_token)
            token.delete()
            return Response({"message":"Logout Successful"})

        except:
            return Response({"message":"Invalid Credentials"})