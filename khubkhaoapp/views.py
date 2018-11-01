from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from khubkhaoapp.models import Item, Veggie, Food

def IndexView(request):
    food_list = Food.objects.all()
    category_list = Item.objects.all()
    veggie_list = Veggie.objects.all()
    context = {
        'food_list': food_list,
        'category_list': category_list,
        'vegie_list': veggie_list,
    }
    return render(request, 'khubkhaoapp/index.html', context)



