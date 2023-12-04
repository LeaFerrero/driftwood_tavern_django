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

    page_names = {
        "menu": 'Menu',
    }

    def get_context_data(self, **kwargs):
        """
        Anula el método get_context_data para incluir datos de contexto personalizados.

        Returns:
            dict: Un diccionario que contiene los datos de contexto base junto con el nombre de la página actual.

        """
        context = super().get_context_data(**kwargs)
        view_name = self.request.resolver_match.url_name
        context["current_page"] = self.page_names.get(view_name, view_name.capitalize())
        return context


class MenuListView(MenuBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS Menu
    """

class MenuDetailView(MenuBaseView,DetailView):
    template_name = "menu_detail.html"
    extra_context = {
        "current_page": "Menu"
    }

class MenuCreateView(MenuBaseView,CreateView):
    template_name = "menu_create.html"
    extra_context = {
        "current_page": "Create"
    }

class MenuUpdateView(MenuBaseView,UpdateView):
    template_name = "menu_create.html"
    extra_context = {
        "current_page": "Update"
    }
    
class MenuDeleteView(MenuBaseView,DeleteView):
    template_name = "menu_delete.html"
    extra_context = {
        "current_page": "Delete"
    }