
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_type = models.CharField(max_length=15,default='admin')
    def __str__(self):
        return self.username

class Company(models.Model):

    
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True,null=True,default='profile_pics/default.jpg')
       

    def __str__(self):
        return self.name

class Jobseeker(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True,null=True,default='profile_pics/default.jpg')

    def __str__(self):
        return self.user.username      


class customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True,null=True,default='profile_pics/default.jpg')

    def __str__(self):
        return self.firest_name + '  ' + self.last_name 


            
class engineer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    district = models.CharField(max_length=50, default=None, blank=True, null=True)
    id_proof = models.FileField(
        max_length = 300,
        upload_to = 'Id_proof/'
    )
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True,null=True,default='profile_pics/default.jpg')    
    

    def __str__(self):
        return self.firest_name + '  ' + self.last_name 


class clubbroker(models.Model):
    CATEGORY = (
        ('induvidual','Induvidual'),
        ('group', 'Group')
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    organisation = models.CharField(
        max_length=20,
        choices=CATEGORY
    )
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True,null=True,default='profile_pics/default.jpg')

    def __str__(self):
        return self.firest_name + '  ' + self.last_name         