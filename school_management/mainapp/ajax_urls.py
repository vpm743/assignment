# mainapp/ajax_urls.py
from django.urls import path
from . import ajax_views

urlpatterns = [
    path('list_schools/', ajax_views.list_schools, name='list_schools'),
    path('list_students/', ajax_views.list_students, name='list_students'),
]