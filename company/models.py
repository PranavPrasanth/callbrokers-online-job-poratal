
from django.db import models
from account.models import User

# Create your models here.

class Vaccany(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.IntegerField()
    experience = models.IntegerField()
    vacancy = models.IntegerField()
    last_date = models.DateField()
    def __str__(self):
        return self.title
