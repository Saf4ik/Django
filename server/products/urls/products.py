from django.urls import path

from products.views import (
    ProductList, ProductDetail, ProductCreate,
    ProductUpdate, ProductDelete
)

app_name = 'products'


urlpatterns = [
    path('<slug:slug>/', ProductDetail.as_view(), name='detail'),
    path('', ProductList.as_view(), name='index'),
    path('create/', ProductCreate.as_view(), name='create'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='delete'),
] 