from django.urls import path 
from .views import (
    UserCreateView,
    UserLogoutView,
    UserLoginView
)
urlpatterns = [
    path('create/',UserCreateView.as_view()),
    path('login/',UserLoginView.as_view()),
    path('logout/', UserLogoutView.as_view())
]
