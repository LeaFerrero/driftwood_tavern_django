from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Menu

# Create your views here.


class MenuBaseView(View):
    template_name = 'menu.html'
    model = Menu
    fields = '__all__'
    success_url = reverse_lazy('menu:all')


class MenuListView(MenuBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS Menu
    """

class MenuDetailView(MenuBaseView,DetailView):
    template_name = "menu_detail.html"

class MenuCreateView(MenuBaseView,CreateView):
    template_name = "menu_create.html"
    extra_context = {
        "tipo": "Create"
    }

class MenuUpdateView(MenuBaseView,UpdateView):
    template_name = "menu_create.html"
    extra_context = {
        "tipo": "Update"
    }

class MenuDeleteView(MenuBaseView,DeleteView):
    template_name = "menu_delete.html"
    extra_context = {
        "tipo": "Delete"
    }