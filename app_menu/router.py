from rest_framework import routers
from .viewsets import MenuViewSet

router = routers.SimpleRouter()

# Registro de la vista del conjunto en la ruta "api_menu"
router.register("api_menu",MenuViewSet)

"""
Router module for the 'menu' application.

This module provides a simple router for the 'MenuViewSet' viewset.
The viewset is registered at the 'api_menu' route.
"""
