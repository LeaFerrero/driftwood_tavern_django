from django.db import models
from django.db.models import Model
from django.core.validators import MaxLengthValidator
from django.core.validators import MinValueValidator

# Create your models here.

class Menu(Model):
    """
    Model representing a menu item.

    Attributes:
        name (str): Name of the menu item.
        description (str): Description of the menu item.
        price_amount (int): Amount of the menu item's price.
        currency (str): Currency type for the price (cp, sp, ep, gp, pp).
        price_unit (str): Unit of measurement for the price (plate, portion, bottle, glass, cup).
        item_type (str): Type of menu item (food, drink).

    Meta:
        db_table (str): Name of the table in the database.
        verbose_name_plural (str): Plural name for the admin interface.

    Methods:
        __str__(): Returns a string representation of the object.
        get_fields(): Returns a list of tuples with the names and values of the object's fields.
    """

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
        ("cup", "Cup")
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
        """
        Returns a string representation of the object.

        Returns:
            str: String representation of the object.
        """
        return f"Name: {self.name}, type: {self.item_type}, price: {self.price_amount} {self.currency}"

    def get_fields(self):
        """
        Returns a list of tuples with the names and values of the object's fields.

        Returns:
            list: List of tuples (name, value) of the object's fields.
        """
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]