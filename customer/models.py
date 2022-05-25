from django.db import models
from account.models import User

# Create your models here.

class Work(models.Model):
    WARRANTY_TYPE = (
        (0, 'No'),
        (1, 'Yes'),
    )
    product_item = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=50)
    model_number = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    warranty = models.IntegerField(choices=WARRANTY_TYPE, default=0)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.product_item

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    subject = models.CharField(max_length=100)
    feedback = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.feedback