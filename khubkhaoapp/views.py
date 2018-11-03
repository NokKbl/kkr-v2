from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from khubkhaoapp.models import Category,EthnicFood, Food
from django.db.models import Q
from django.urls import reverse

class IndexTemplateView(TemplateView):
    template_name = 'khubkhaoapp/index.html'
    def get_context_data(self,*args,**kwargs):
        context = super(IndexTemplateView,self).get_context_data(*args, **kwargs)
        food_list = Food.objects.all()
        category_list = Category.objects.all()
        ethnic_list = EthnicFood.objects.all()
        context = {
            'food_list': food_list,
            'category_list': category_list,
            'ethnic_list': ethnic_list,
        }
        return context


def IndexSearchView(request):
    my_ethnic = request.POST
    my_category = request.POST

    try:
        my_ethnic = request.POST.getlist('ethnic_name')
        my_category = request.POST.getlist('category_name')
    except (KeyError, Food.DoesNotExist):
        pass

    else:
        selected_ethnic = EthnicFood.objects.filter(id__in=my_ethnic)
        selected_category = Category.objects.filter(id__in=my_category)
        # food_list = Food.objects.filter(Q(ethnic_food_name__in=selected_ethnic)|Q(category__in=selected_category))
        food_list = Food.objects.filter(ethnic_food_name__in=selected_ethnic).filter(category__in=selected_category)
        category_list = Category.objects.all()
        ethnic_list = EthnicFood.objects.all()
        context = {
            'food_list': food_list,
            'category_list': category_list,
            'ethnic_list': ethnic_list,
        }
    # return HttpResponseRedirect(reverse('khubkhaoapp:result', context))
    return render(request, 'khubkhaoapp/index.html', context)
