from django.http import HttpResponse
from django.shortcuts import redirect ,render

def home(request):
    return render(request,'myhomecb/home.html')

def jobseeker_index(request):
    
    return render(request,'jobseeker/jobseeker.html') 



   


  
       


    

# Create your views here.
