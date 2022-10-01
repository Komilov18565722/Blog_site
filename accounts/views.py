from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserChangeFrom, CustomUserCreationFrom
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationFrom
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# class ChangePasswordView(UpdateView):
#     form_class = CustomUserChangeFrom
#     # success_url = reverse_lazy('home')
#     template_name = 'registration/password_change_form.html'