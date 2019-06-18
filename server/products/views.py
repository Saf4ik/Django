import json
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Product, Category
from .forms import CategoryForm

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

def category_create(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            # Category.objects.create(
            #     name=form.cleaned_data.get('name'),
            #     description=form.cleaned_data.get('description')
            # )
            form.save()
            return redirect(
                reverse('products:index')
            )
    return render(
        request,
        'categories/create.html',
        {'form': form}
    )
