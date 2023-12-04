from django.db import models
from django.db.models import Model
from django.core.validators import MaxLengthValidator
from django.core.validators import MinValueValidator

# Create your models here.

class Menu(Model):

    TYPE_CHOICES = [
        ('dish', 'Dish'),
        ('drink', 'Drink'),
    ]

    CURRENCY_CHOICES = [
        ("cp", "cp"),
        ("sp", "sp"),
        ("ep", "ep"),
        ("gp", "gp"),
        ("pp", "pp"),
    ]

    name = models.CharField(
        max_length=255, 
        blank=False, 
        null=False, 
        validators=[MaxLengthValidator(255, message="Max 255 characters.")]
        )
    
    description = models.TextField(
        blank=False, 
        null=False, 
        validators=[MaxLengthValidator(255, message="Max 255 characters.")]
        ) 
    
    price_amount = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1, message="Must be greater than 0.")]
        )
    
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    
    item_type = models.CharField(max_length=10, choices=TYPE_CHOICES)


    class Meta:
        db_table = "dwt_menu_items"
        verbose_name_plural = "Menu Items"

    def __str__(self):
        return f"Name: {self.name}, detail: {self.item_type}, price: {self.price_amount} {self.currency}"

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]