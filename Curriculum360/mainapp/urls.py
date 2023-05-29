from  django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
   
    path('dash', views.dash, name='dashboard')
]