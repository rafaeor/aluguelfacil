from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import InquilinoSignUpForm


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type == 'proprietario':
                return redirect('core:painel_proprietario')
            return redirect('core:painel_inquilino')
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.user_type == 'proprietario':
            return reverse_lazy('core:painel_proprietario')
        return reverse_lazy('core:painel_inquilino')


class SignUpView(CreateView):
    form_class = InquilinoSignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type == 'proprietario':
                return redirect('core:painel_proprietario')
            return redirect('core:painel_inquilino')
        return super().get(request, *args, **kwargs)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')
