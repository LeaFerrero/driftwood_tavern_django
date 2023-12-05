from rest_framework.viewsets import ModelViewSet
from .models import Menu
from .serializers import MenuSerializer

class MenuViewSet(ModelViewSet):
    """
    Viewset for the Menu model.

    Attributes:
        queryset (QuerySet): Data set for the view (all Menu objects).
        serializer_class (class): Serializer class to use (MenuSerializer).
    """
    
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer