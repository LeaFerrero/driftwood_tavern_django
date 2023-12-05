from django.contrib import admin
from django.urls import path , include
from .router import router

from .views import *

app_name = "menu"

urlpatterns = [
    path("", MenuListView.as_view(), name="all"),
    path("create/", MenuCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", MenuDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", MenuUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", MenuDeleteView.as_view(), name="delete"),
]

urlpatterns += router.urls

"""
URL patterns for the 'menu' application.

- "" : All menu items
- "create/" : Create a new menu item
- "<int:pk>/detail/" : Detailed view for a specific menu item
- "<int:pk>/update/" : Update view for a specific menu item
- "<int:pk>/delete/" : Delete view for a specific menu item
"""