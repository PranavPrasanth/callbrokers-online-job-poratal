from django.urls import path
from.views import *
urlpatterns = [

path('',home,name='index'),

path('signup/jobseeker/',signup_Jobseeker,name='account_signup_jobseeker'),
path('signup/company/',signup_Company,name='account.signup_company'),
path('signup/customer/',signup_customer,name='account.signup_customer'),
path('signup/clubbroker/',signup_clubbroker,name='account.signup_clubbroker'),
path('signup/engineer/',signup_engineer,name='account.signup_engineer'),
path('login/', login_view, name='account_login'),
path('logout/', logout_view,name='account_logout'),
] 