from django.urls import path
from .views import my_list
urlpatterns=[
    path('',my_list,name='my_app')
]