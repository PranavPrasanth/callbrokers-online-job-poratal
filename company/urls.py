from django.urls import path
from .views import *

urlpatterns = [
    path('',company_index,name='company_home'),
    path('profile/',profile,name='company_profile'),
    path('change_password/',change_password,name='company_change_password'),
    path('create_work/',create_work,name='company_create_work'),
    path('create_vaccancy/',create_vaccancy,name='company_create_vaccancy'),
    path('search_engineers/',search_engineers,name='company_search_engineers'),
    path('manage_work/', work_list, name='company_manage_work'),
    path('edit_work/<int:work_id>/', edit_work, name='company_edit_work_detail'),
    path('delete_work/<int:work_id>/', delete_work, name='company_delete_work_detail'),
    path('vaccancy_list/',vaccancy_list,name='company_vaccancy_list'),
    path('edit_vaccancy/<int:v_id>/', edit_vaccancy, name='company_edit_vaccancy_detail'),
    path('delete_vaccancy/<int:v_id>/', delete_vaccancy, name='company_delete_vaccancy_detail'),
    path('job_applications/',job_application_list,name='company_job_applications'),
    path('application/accept/<int:app_id>/',accept_application,name='company_accept_application'),
    path('application/reject/<int:app_id>/',reject_application,name='company_reject_application'),
    path('work_request/',work_request,name='company_work_request'),
    path('approve_work/<int:app_work_id>/',approve_work,name='company_approve_work'),
    path('reject_work/<int:app_work_id>/',reject_work,name='company_reject_work'),
    path('track_work/',track_work,name='company_track_work'),
    path('work_detail/<int:work_id>/',open_report,name='company_work_detail'),
]
