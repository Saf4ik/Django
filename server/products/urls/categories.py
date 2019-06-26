from django.urls import path

from products.views import (
    CategoryCreate, CategoryUpdate, CategoryDelete,
    CategoryList, CategoryDetail
)

app_name = 'categories'


urlpatterns = [
    path('create/', CategoryCreate.as_view(), name='create'),
    path('<int:pk>/update/', CategoryUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', CategoryDelete.as_view(), name='delete'),
    path('<slug:slug>/', CategoryDetail.as_view(), name='detail'),
    path('', CategoryList.as_view(), name='index'),
]