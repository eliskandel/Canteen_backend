from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

    def create(self, validated_data):
        request=self.context['request']
        password=validated_data.pop('password')
        
        user=User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)
    
class UserLogoutSerializer(serializers.Serializer):
    token=serializers.CharField(required=True)