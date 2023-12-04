from django.db import models
from django.db.models import Model
from django.core.validators import MaxLengthValidator
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

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

    UNIT_CHOICES = [
        ("plate", "Plate"),
        ("portion", "Portion"),
        ("bottle", "Bottle"),
        ("glass", "Glass"),
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
    
    price_unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    
    item_type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    class Meta:
        db_table = "dwt_menu_items"
        verbose_name_plural = "Menu Items"

    def __str__(self):
        return f"Name: {self.name}, type: {self.item_type}, price: {self.price_amount} {self.currency}"

    
    def clean(self):
        if self.item_type == 'food' and self.price_unit not in ['portion', 'plate']:
            raise ValidationError("For food, price_unit must be 'portion' or 'plate'.")
        elif self.item_type == 'drink' and self.price_unit not in ['bottle', 'glass']:
            raise ValidationError("For drink, price_unit must be 'bottle' or 'glass'.")

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]