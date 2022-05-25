from django.urls import path
from .views import *

urlpatterns = [
    path('',jobseeker_index,name='jobseeker_home'),
    path('profile/',profile,name='jobseeker_profile'),
    path('change_password/',change_password,name='jobseeker_change_password'),
    path('company_list/',company_list,name='jobseeker_company_list'),
    path('job_list/<int:company_id>/',job_list,name='jobseeker_job_list'),
    path('applay_job/',job_applied,name='jobseeker_applay_job'),
    path('delete_applied_job/<int:job_id>/',delete_applied_job,name='jobseeker_delete_applied_job'),
    path('feedback/', feedback, name="jobseeker_feedback"),
]