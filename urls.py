"""NearbyAgents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('NewYork/',views.getAgents, name='NewYork'),
    path('Boston/',views.getAgentsofBoston, name='Boston'),
    path('LA/',views.getAgentsofLA, name='LA'),
    path('Chicago/',views.getAgentsofChicago, name='Chicago'),
    path('Huston/',views.getAgentsofHuston, name='Huston'),
    path('Pheonix/',views.getAgentsofPheonix, name='Pheonix'),
    path('SanDiego/',views.getAgentsofSanDiego, name='SanDiego'),
    path('Dallas/',views.getAgentsofDallas, name='Dallas'),
    path('SanJose/',views.getAgentsofSanJose, name='SanJose'),
    path('Austin/',views.getAgentsofAustin, name='Austin'),
    path('Columbus/',views.getAgentsofColumbus, name='Columbus'),
    path('updateAgentsDistance/',views.updateAgentsDistance, name='updateAgentsDistance'),
    path('',views.mainpage, name='Home')
]
