from django.urls import path
from .views import *

urlpatterns = [
    path('',engineer_index,name='engineer_home'),
    path('profile/',profile,name='engineer_profile'),
    path('change_password/',change_password,name='engineer_change_password'),
    path('work_list/',work_list,name='engineer_work_list'),
    path('apply/work/<int:work_id>/',apply_work,name='engineer_apply_work'),
    path('applied_work/',applied_work,name='engineer_applied_work'),
    path('approved_work/',approved_work,name='engineer_approved_work'),
    path('report/create/', create_report, name='engineer_create_report')
]