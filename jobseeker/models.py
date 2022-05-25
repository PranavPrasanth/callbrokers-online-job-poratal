from django.db import models
from account.models import User, Jobseeker
from company.models import Vaccany

# Create your models here.

class ApplayJob(models.Model):
    jobseeker = models.ForeignKey(Jobseeker,on_delete=models.CASCADE)
    job = models.ForeignKey(Vaccany,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,default='Pending')
    def __str__(self):
        return self.jobseeker.user.username
