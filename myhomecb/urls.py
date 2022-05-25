from django.urls import path
from .views import * 

urlpatterns = [
# path('',home,name='index'),    
path('',home, name='home'),
path('',jobseeker_index,name='jobseeker_home'),
# path('company/',company,name='myhome_company'),
# path('customer/',customer,name='myhome_customer'),
# path('engineer/',engineer,name='myhome_engineer'),
# path('jobseeker/',jobseeker,name='myhome_jobseeker'),
# path('clubbroker',clubbroker,name='myhome_clubbroker'),

]