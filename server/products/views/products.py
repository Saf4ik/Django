import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import (
    ListView, DetailView
)
from products.models import Product, Category

class ProductList(ListView):
    model = Product
    template_name = 'products/index.html'
    


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/detail.html'
    
    


# Create your views here.
def product_list(request):
    # with open('products/fixtures/data.json', 'rb') as file:
    #     return render(
    #         request, 
    #         'products/index.html',
    #         {'products': json.load(file)}
    #         )
    return render(
        request,
        'products/index.html',
        {
            'products': Product.objects.all()
        }
    )

def product_detail(request, pk):
    # with open('products/fixtures/data.json', 'rb') as file:
    #     return render(
    #         request,
    #         'products/detail.html',
    #          {'product': json.load(file)[pk]}
    #     )
    return render(
        request,
        'products/detail.html',
        {
            'product': Product.objects.get(pk=pk)
        }
    )


