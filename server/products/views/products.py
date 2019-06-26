import json
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView
)
from products.models import Product, Category


class ProductCreate(CreateView):
    model = Product
    template_name = 'products/create.html'
    fields = ['name', 'category', 'description', 'image', 'cost']
    success_url = reverse_lazy('products:index')

 
class ProductUpdate(UpdateView):
    model = Product
    template_name = 'products/update.html'
    fields = ['name', 'category', 'description', 'image', 'cost']
    success_url = reverse_lazy('products:index')


class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:index')


class ProductList(ListView):
    model = Product
    template_name = 'products/index.html'
    paginate_by = 3
    

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/detail.html'
    slug_field = 'name'
    
    


# Create your views here.
# def product_list(request):
#     # with open('products/fixtures/data.json', 'rb') as file:
#     #     return render(
#     #         request, 
#     #         'products/index.html',
#     #         {'products': json.load(file)}
#     #         )
#     return render(
#         request,
#         'products/index.html',
#         {
#             'products': Product.objects.all()
#         }
#     )

# def product_detail(request, pk):
#     # with open('products/fixtures/data.json', 'rb') as file:
#     #     return render(
#     #         request,
#     #         'products/detail.html',
#     #          {'product': json.load(file)[pk]}
#     #     )
#     return render(
#         request,
#         'products/detail.html',
#         {
#             'product': Product.objects.get(pk=pk)
#         }
#     )


