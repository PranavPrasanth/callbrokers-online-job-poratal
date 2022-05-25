from django.urls import path
from .views import *

urlpatterns = [
    path('',customer_index,name='customer_home'),
    path('profile/',profile,name='customer_profile'),
    path('change_password/',change_password,name='customer_change_password'),
    path('create_work/',create_work,name='customer_create_work'),
    path('search_engineers/',search_engineers,name='customer_search_engineers'),
    path('manage_work/',manage_work,name='customer_manage_work'),
    path('edit_work/<int:work_id>/',edit_work,name='customer_edit_work'),
    path('delete_work/<int:work_id>/',delete_work,name='customer_delete_work'),
    path('work_request/',work_request,name='customer_work_request'),
    path('approve_work/<int:app_work_id>/',approve_work,name='customer_approve_work'),
    path('reject_work/<int:app_work_id>/',reject_work,name='customer_reject_work'),
    path('feedback/',feedback,name='customer_feedback'),
    path('track_work/',track_work,name='customer_track_work'),
    path('work_detail/<int:work_id>/',open_report,name='customer_work_detail'),
]