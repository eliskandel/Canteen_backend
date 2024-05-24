from django.db import models
from user.models import User
# Create your models here.
class Product(models.Model):
    image=models.ImageField(upload_to="./product/images", default='')
    name=models.CharField(max_length=100, null=False)
    description=models.TextField()
    price=models.FloatField(null=False, blank=False)
    
    def __str__(self) -> str:
        return self.name