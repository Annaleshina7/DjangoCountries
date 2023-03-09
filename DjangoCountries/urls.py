"""DjangoCountries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import main.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('countries-list/', views.countries_list, name='countries-list'),
    path('countries-list/<str:letter>/', views.countries_list, name='countries-list'),
    path('languages-list/', views.languages_list, name='languages-list'),
    path('country/<int:id>/', views.country, name='country'),
    path('language/<int:id>/', views.language, name='language'),
    path('import/', views.import_countries, name='import'), # для переноса данных
    path('admin/', admin.site.urls)
]
