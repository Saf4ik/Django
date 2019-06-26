from django.urls import path
from .views import (
    login_view, AccountLoginView, AccountLogoutView
)


app_name = 'accounts'

urlpatterns = [
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('', AccountLoginView.as_view(), name='login'),
]