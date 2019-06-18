from django.urls import path

from products.views import (
    product_list, product_detail, category_create,
    ProductList, ProductDetail,
)

app_name = 'products'


urlpatterns = [
    path('<int:pk>', ProductDetail.as_view(), name='detail'),
    path('', ProductList.as_view(), name='index'),
] 