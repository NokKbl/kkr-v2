from django.db import models

class Country(models.Model):
    country_name = models.CharField(
        max_length=20,
        verbose_name='Category name',
        unique=True,
        blank=False,
        help_text='Enter country name'
    )
    
    def __str__(self):
        return self.country_name

class Category(models.Model):
    type_name = models.CharField(
        max_length=20,
        verbose_name='Category name',
        unique=True,
        blank=False,
        help_text='Enter Category name'
    )
    def __str__(self):
        return self.type_name

class Food(models.Model):
    food_name = models.CharField(
        max_length=20,
        verbose_name='Food name',
        unique=True,
        blank=False,
        help_text='Enter food name'
    )

    image_location = models.CharField(
        max_length=100,
        verbose_name='Image url',
        unique=True,
        blank=False,
        help_text='Enter url location'
    )

    average_price = models.PositiveIntegerField(
        default=0,
        verbose_name='Average price'
    )

    rate = models.PositiveIntegerField(
        default=0,
        verbose_name='Average price'
    )

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        verbose_name='Country Food'
    )
    
    def __str__(self):
        return self.food_name
    
    def get_average_price(self):
        return self.average_price
    
    def get_image_location(self):
        return self.image_location
    
    def get_rate(self):
        return self.rate
