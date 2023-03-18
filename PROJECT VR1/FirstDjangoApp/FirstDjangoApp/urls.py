
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from SecondModule import views as SecondModule_views
from FirstModule import views as FirstModule_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('FirstModule/', include('FirstModule.urls')),
    path('SecondModule/', include('SecondModule.urls')),
    path('About-us-only', SecondModule_views.Aboutus, name='Aboutus'),
    path('index/', SecondModule_views.index, name='Aboutus'),
]
