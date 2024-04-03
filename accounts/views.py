from django.views.genric import CreateView
from django.urls import reverse_lazy
from .form import CustomUserChangeForm


class SignUpView(CreateView):
    template_name = "regisration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")

# Create your views here.
