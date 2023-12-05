from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Menu

# Create your views here.


class MenuBaseView(View):
    """
    Base view for CRUD operations on the Menu model.

    Attributes:
        template_name (str): Name of the HTML template to use.
        model (class): Associated model class.
        fields (list): List of fields to include in forms (optional).
        success_url (str): URL to redirect to after a successful operation.
    """

    template_name = 'menu.html'
    model = Menu
    fields = '__all__'
    success_url = reverse_lazy('menu:all')
    


class MenuListView(MenuBaseView,ListView):
    """
    View to display a list of Menu objects.

    Extra Attributes:
        - None
    """
    extra_context = {
        "current_page": "Menu"
    }

class MenuDetailView(MenuBaseView,DetailView):
    """
    View to display details of a Menu object.

    Extra Attributes:
        template_name (str): Name of the HTML template for the detailed view.
        extra_context (dict): Additional context to pass to the template.
    """

    template_name = "menu_detail.html"
    extra_context = {
        "current_page": "Detail"
    }

class MenuCreateView(MenuBaseView,CreateView):
    """
    View to create a new Menu object.

    Extra Attributes:
        template_name (str): Name of the HTML template for creation.
        extra_context (dict): Additional context to pass to the template.
    """

    template_name = "menu_create.html"
    extra_context = {
        "current_page": "Create"
    }

class MenuUpdateView(MenuBaseView,UpdateView):
    """
    View to update an existing Menu object.

    Extra Attributes:
        template_name (str): Name of the HTML template for updating.
        extra_context (dict): Additional context to pass to the template.
    """


    template_name = "menu_create.html"
    extra_context = {
        "current_page": "Update"
    }
    
class MenuDeleteView(MenuBaseView,DeleteView):
    """
    View to delete a Menu object.

    Extra Attributes:
        template_name (str): Name of the HTML template for deletion.
        extra_context (dict): Additional context to pass to the template.
    """

    template_name = "menu_delete.html"
    extra_context = {
        "current_page": "Delete"
    }