from django.urls import path

from products.views import (
    category_create, category_update, category_delete,
    CategoryCreate, CategoryUpdate, CategoryDelete,
)

app_name = 'categories'


urlpatterns = [
    path('create/', CategoryCreate.as_view(), name='create'),
    path('<int:pk>/update/', CategoryUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', CategoryDelete.as_view(), name='delete'),
] 