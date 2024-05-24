from django.urls import path
from .views import (
    ProductCreateView,
    ProductDeletView,
    ProductListView,
    ProductRetrieveView,
    ProductUpdateView,
)
urlpatterns = [
    path('',ProductListView.as_view()),
    path('read/<int:pk>/',ProductRetrieveView.as_view()),
    path('delete/<int:pk>/',ProductDeletView.as_view()),
    path('update/<int:pk>/',ProductUpdateView.as_view()),
    path('create/',ProductCreateView.as_view()),
]
