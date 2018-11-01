from django.contrib import admin
from .models import Food,Ingredient,Item,Veggie

class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 1

class FoodAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['food_name']}),
        ('Details',     {'fields': ['image_location','average_price']}),
        ('Veggie',      {'fields': ['veggie']}),
    ]
    inlines = [IngredientInline]

admin.site.register(Food, FoodAdmin)
admin.site.register(Veggie)
admin.site.register(Item)