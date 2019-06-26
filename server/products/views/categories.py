import json
from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.views.generic import (
    CreateView, UpdateView, DeleteView,
    ListView, DetailView
)
from django.core.paginator import Paginator
from django.urls import (
    reverse, reverse_lazy
)
from products.models import Category
from products.forms import CategoryForm

class CategoryCreate(CreateView):
    model = Category
    template_name = 'categories/create.html'
    success_url = reverse_lazy('products:index')
    form_class = CategoryForm
    

class CategoryUpdate(UpdateView):
    model = Category
    template_name = 'categories/update.html'
    success_url = reverse_lazy('products:index')
    form_class = CategoryForm


class CategoryDelete(DeleteView):
    model = Category
    template_name = 'categories/delete.html'
    success_url = reverse_lazy('products:index')
    

class CategoryList(ListView):
    model = Category
    template_name = 'categories/index.html'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'categories/detail.html'
    slug_field = 'name'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        category = context.get('object')
        paginator = Paginator(category.products.all().prefetch_related('products'), self.paginate_by)
        page_number = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page_number)
        return context


# def category_create(request):
#     form = CategoryForm()
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             # Category.objects.create(
#             #     name=form.cleaned_data.get('name'),
#             #     description=form.cleaned_data.get('description')
#             # )
#             form.save()
#             return redirect(
#                 reverse('products:index')
#             )
#     return render(
#         request,
#         'categories/create.html',
#         {'form': form}
#     )

# def category_update(request, pk):
#     obj = get_object_or_404(Category, pk=pk)
#     form = CategoryForm(instance=obj)

#     if request.method == 'POST':
#         form = CategoryForm(
#             request.POST, instance=obj
#             )
#         if form.is_valid():
#             form.save()
#             return redirect(
#                 reverse('products:index')
#             )

#     return render(
#         request, 'categories/update.html',
#         { 'form': form }
#     )


# def category_delete(request, pk):
#     obj = get_object_or_404(Category, pk=pk)

#     if request.method == 'POST':
#         obj.delete()
#         return redirect(
#             reverse('products:index')
#             )

#     return render(
#         request, 'categories/delete.html',
#         { 'object': obj }
#     )