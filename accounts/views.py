from django.urls import reverse
from django.views.generic.edit import CreateView
from accounts.forms import SingUpForm
from django.contrib import messages
from accounts.models import User
from django.contrib.auth.views import LoginView

# Create your views here.


class SingupPageView(CreateView):
    form_class = SingUpForm
    context_object_name = "froms"
    model = User
    template_name = "singup.html"

    def form_valid(self, form):
        messages.success = "user account create sucess fully "

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("home:home")


class LoginPageView(LoginView):
    template_name = "login.html"

    def get_success_url(self) -> str:
        return reverse("home:home")
