from django.urls import path

from .views import (
    product_list, product_detail, category_create,
)

app_name = 'products'


urlpatterns = [
    path('create/', category_create, name='create'),
    path('', product_list, name='index'),
    path('<int:pk>/', product_detail, name='detail'),
] 