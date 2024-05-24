from rest_framework import serializers
from .models import Order, Product
from product.serializer import ProductSerializer
from user.serializer import UserSerializer
class OrderListSerializer(serializers.ModelSerializer):
    product=ProductSerializer()
    user=UserSerializer()
    class Meta:
        model = Order
        fields = ['id', 'product', 'quantity', 'total_price','user']

class OrderSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

    class Meta:
        model = Order
        fields = ['id', 'product_id', 'quantity', 'total_price']
        read_only_fields = ['total_price']

    def create(self, validated_data):
        product_id = validated_data.pop('product_id')
        quantity = validated_data.pop('quantity')
        product = Product.objects.get(pk=product_id)
        total_price = product.price * quantity
        existing_order = Order.objects.filter(
            user=self.context['request'].user,
            product=product
        ).first()

        if existing_order:
            existing_order.quantity += quantity
            existing_order.total_price = product.price * existing_order.quantity
            existing_order.save()
            return existing_order
        else:
            order = Order.objects.create(
                user=self.context['request'].user,
                product=product,
                quantity=quantity,
                total_price=total_price
            )
            return order
