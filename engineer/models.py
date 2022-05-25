from django.db import models
from account.models import User, engineer
from customer.models import Work
# Create your models here.

class ApplyWork(models.Model):
    engineer = models.ForeignKey(engineer, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    status = models.CharField(default='Applied', max_length=20)
    date = models.DateTimeField(auto_now_add=True)

class Report(models.Model):
    description = models.TextField()
    file = models.FileField(
        verbose_name="Report",
        upload_to="reports"
        )
    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )
    work  = models.ForeignKey(
        to=ApplyWork,
        on_delete=models.CASCADE
    )
    

