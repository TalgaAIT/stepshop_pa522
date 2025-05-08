from django.shortcuts import render

from mainapp.models import Product


def index(request):
    title = 'главная страница'

    prods = Product.objects.all()[:4]

    context = {
        'title': title,
        'products': prods,
    }

    return render(request, 'index.html', context)

def contacts(request):
    return render(request, 'contact.html')
