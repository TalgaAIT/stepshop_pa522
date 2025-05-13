from itertools import product

from django.urls import path

from mainapp.views import index, contacts

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contact'),
    # path('about/', about, name='about'),
    # path('products/', products, name='products'),
    # path('product', product, name='product'),
]
