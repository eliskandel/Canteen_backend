from django.urls import path
from .views import BuyProductView, OrderListView,OrderDeleteView,OrderUpdateView

urlpatterns = [
    path('buy/', BuyProductView.as_view()),
    path('', OrderListView.as_view()),
    path('delete/<int:pk>/',OrderDeleteView.as_view()),
    path('update/<int:pk>/',OrderUpdateView.as_view())
    
]