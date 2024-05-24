from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    category=models.CharField(max_length=10, null=False, blank=False, default="buyer")
    def __str__(self) -> str:
        return self.username
    