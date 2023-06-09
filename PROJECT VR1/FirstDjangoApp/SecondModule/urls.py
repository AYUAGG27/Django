"""FirstDjangoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from SecondModule import views
from django.urls import path

urlpatterns = [

    path('', views.SecondModule, name='SecondModule'),
    path('delete/<user_id>', views.deleteuser, name='deleteuser'),
    path('checkadmin/<user_id>', views.isadmin, name='checkadmin'),
    path('checkstudent/<user_id>', views.isadmin, name='checkstudent'),
    path('edituser/<user_id>', views.edituser, name='edituser'),
    path('index', views.index, name='index'),
    path('About-us-only', views.Aboutus, name='Aboutus'),
    path('addEvents', views.addEvents, name='addEvents')
]
