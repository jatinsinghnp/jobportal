from django.urls import path
from accounts.views import SingupPageView, LoginPageView

app_name = "account"
urlpatterns = [
    path("singup", SingupPageView.as_view(), name="singup"),
    path("login", LoginPageView.as_view(), name="login"),
]
