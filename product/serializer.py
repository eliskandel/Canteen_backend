from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        
    def create(self, validated_data):
        request=self.context['request']
        
        if request.user.category == 'seller':
            product=Product.objects.create(**validated_data)
            return product
        else:
            raise serializers.ValidationError("Category does not meet requirement")