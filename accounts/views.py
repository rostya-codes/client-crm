from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from .forms import UserRegisterForm, EmailLoginForm


class RegisterView(FormView):
    template_name = 'accounts/register.html'  # путь к шаблону
    form_class = UserRegisterForm
    success_url = reverse_lazy('accounts:login')  # после регистрации перенаправление

    def form_valid(self, form):
        form.save()  # создаёт пользователя
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = EmailLoginForm
    success_url = reverse_lazy('clients:home')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        if not email or not password:
            form.add_error(None, 'Email и пароль должны быть заполнены.')
            return self.form_invalid(form)

        user = authenticate(self.request, username=email, password=password)
        if user is None:
            form.add_error(None, 'Неверный email или пароль.')
            return self.form_invalid(form)

        login(self.request, user)
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('clients:home')
