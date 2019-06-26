from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.urls import reverse
from .forms import AccountLoginForm


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = AccountLoginForm


class AccountLogoutView(LogoutView):
    template_name = 'accounts/logout.html'


def login_view(request):
    form = AccountLoginForm()
    success_url = reverse('main:index')

    if request.method == 'POST':
        form = AccountLoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(
                username=username,
                password=password
            )

            if user and user.is_active:
                login(request, user)
                return redirect(success_url)

    return render(
        request, 'accounts/login.html',
        {'form': form}
    )
