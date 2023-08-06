"""
URL configuration for project14 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('table/',table,name='table'),
    path('img_rotate/',img_rotate,name='img_rotate'),
    path('nav/',nav,name='nav'),
    path('img/',img,name='img'),
    path('a_response/',a_response,name='a_response'),
    path('x/',x,name='x'),
    path('reg_form/',reg_form,name='reg_form'),
    path('new/',new,name='new'),
    path('box/',box,name='box'),
    path('arth/',arth,name='arth'),
    path('appli/',appli,name='appli'),
    path('jsp/',jsp,name='jsp'),
    path('jsp1/',jsp1,name='jsp1'),
    path('amz/',amz,name='amz'),
    path('form/',form,name='form'),
    path('convert/',convert,name='convert'),
]
