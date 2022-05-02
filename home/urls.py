from django.urls import path
from .views import HomePageView, CompanyPageView

app_name = "home"


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("company/", CompanyPageView.as_view(), name="company"),
]
