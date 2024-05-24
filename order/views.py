from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from .serializer import (
    OrderSerializer,OrderListSerializer
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Order

# Create your views here.
class BuyProductView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        if user.category == 'seller':  # Assuming you have a boolean field is_seller in your user model
            # If the user is a seller, show every order
            return Order.objects.all()
        else:
            # If the user is not a seller, return an empty queryset (or any other logic as needed)
            return Order.objects.filter(user=self.request.user)
        
    

class OrderDeleteView(DestroyAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
class OrderUpdateView(UpdateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    