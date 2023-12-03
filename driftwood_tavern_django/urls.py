"""
URL configuration for driftwood_tavern_django project.

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
from django.urls import path, include
from .views import *



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexTemplate.as_view(), name="index"),
    path("location/", LocationTemplate.as_view(), name="location"),
    path("contact_form/", ContactFormTemplate.as_view(), name="contact_form"),
    path("our_history/", OutHistoryTemplate.as_view(), name="our_history"),
    path("potions_catalog/", PotionsCatalogTemplate.as_view(), name="potions_catalog"),
    path("menu/", include("app_menu.urls"))
]
