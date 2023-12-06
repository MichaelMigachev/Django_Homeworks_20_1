from django.shortcuts import render
from catalog.models import Product

# Create your views here.

def index(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title': 'Главная'
    }
    return render(request, 'catalog/index.html', context)


def categories(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'каталог'
    }
    return render(request, 'catalog/categories.html', context)