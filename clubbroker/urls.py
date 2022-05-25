from django.urls import path
from .views import *

urlpatterns = [
    path('',clubbroker_index,name='clubbroker_home'),
    path('profile/',profile,name='clubbroker_profile'),
    path('change_password/',change_password,name='clubbroker_change_password'),
    path('search_engineers/',search_engineers,name='clubbroker_search_engineers'),
    path('work_list/', work_list, name="clubbroker_work_list"),
]
