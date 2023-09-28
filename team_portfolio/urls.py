"""
URL configuration for team_portfolio project.

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

import main.views as main_views
import max.views as max_views
import taisia.views as taisia_views
import egor.views as egor_views
import artem.views as artem_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.main, name='main'),
    path('max', max_views.max, name='max'),
    path('taisia', taisia_views.taisia, name='taisia'),
    path('egor', egor_views.egor, name='egor'),
    path('artem', artem_views.artem, name='artem'),
]
