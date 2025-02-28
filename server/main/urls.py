from django.urls import path

from main.views import (
    index, about, contacts,
)

app_name = 'main'


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
] 