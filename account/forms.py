from django import forms
from account.models import  Jobseeker,Company,User,customer,clubbroker,engineer


class signupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User 
        fields = ['first_name','last_name','email','username']
        help_texts = {
            'username': None,
        }

class CommonForm(forms.ModelForm):
    """Form definition for Common."""

    class Meta:
        """Meta definition for Commonform."""

        model = User
        fields = ('first_name', 'last_name', 'email')


    
class AuthForm(forms.ModelForm):
    """Form definition for Auth."""

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        """Meta definition for Authform."""

        model = User
        fields = ('username','password')
        widget = {
            'password': forms.PasswordInput(),
        }
        help_texts ={
            'username': None
        }



class EditProfileForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ['first_name','last_name','email','username']
            help_texts = {
                'username': None,
            
            }    

class CompanyForm(forms.ModelForm):


         """Form deefinition for Company """
         class Meta:
             """Meta definition for Companyform"""
             model = Company
             exclude = ['user']
   
class JobseekerForm(forms.ModelForm):


         """Form deefinition for company """
         class Meta:
             """Meta definition for companyform."""
             model = Jobseeker
             exclude = ['user']




class engineerForm(forms.ModelForm):


         """Form deefinition for Company """
         class Meta:
             """Meta definition for Companyform"""
             model = engineer
             exclude = ['user']
   
class clubbrokerForm(forms.ModelForm):


         """Form deefinition for company """
         class Meta:
             """Meta definition for companyform."""
             model = clubbroker
             exclude = ['user']


  
class customerForm(forms.ModelForm):


         """Form deefinition for Company """
         class Meta:
             """Meta definition for Companyform"""
             model = customer
             exclude = ['user']
   
                  