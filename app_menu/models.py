from django.db import models
from django.db.models import Model

# Create your models here.

class Menu(Model):

    TYPE_CHOICES = [
        ('food', 'Food'),
        ('drink', 'Drink'),
    ]

    CURRENCY_CHOICES = [
        ("cp", "cp"),
        ("sp", "sp"),
        ("ep", "ep"),
        ("gp", "gp"),
        ("pp", "pp"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=False) 
    price_amount = models.PositiveIntegerField(null=False, blank=False, default=1)
    currency = models.CharField(max_length=2, choices=CURRENCY_CHOICES, default="cp")
    item_type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    class Meta:
        db_table = "dwt_menu_items"
        verbose_name_plural = "Menu Items"

    def __str__(self):
        return f"Name: {self.name}, detail: {self.item_type}, price: {self.price}"

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]