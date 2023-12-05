from rest_framework.serializers import ModelSerializer
from .models import Menu

class MenuSerializer(ModelSerializer):
    """
    Serializer for the Menu model.

    Attributes:
        Meta.model (class): Model associated with the serializer (Menu).
        Meta.fields (list): List of fields to include in serialization (all).
    """

    class Meta:
        model = Menu
        fields = "__all__"