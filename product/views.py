from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from .models import Product
# Create your views here.
from .serializer import(
    ProductSerializer,

)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ProductCreateView(CreateAPIView):
    serializer_class=ProductSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

class ProductRetrieveView(RetrieveAPIView):
    serializer_class=ProductSerializer
    def get_queryset(self):
        pk=self.kwargs.get('pk')
        return Product.objects.filter(id=pk)
    
class ProductUpdateView(UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user)
    
class ProductDeletView(DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user)
    
class ProductListView(ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer