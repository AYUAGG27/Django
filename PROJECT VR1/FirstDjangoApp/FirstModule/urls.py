from unicodedata import name
from FirstModule import views
from django.urls import path

urlpatterns = [
    path('', views.FirstModule, name='FirstModule')

   
]