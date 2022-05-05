import email
from django.shortcuts import render
from django.views.generic import ListView
from job.models import Company, Job
from django.db.models import Q
from home.forms import CompanyForm
from django.views.generic import CreateView
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

# Create your views here.


class HomePageView(ListView):
    template_name = "index.html"
    model = Job
    context_object_name = "jobs"

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .values(
                "company",
                "title",
                "location",
                "salary",
                "types",
                "creation_date",
            )
        )

    def post(self, request, *args, **kwargs):
        if self.request.method == "POST":
            location = self.request.POST.get("locate")
            job = self.request.POST.get("job")
        print(f"{location}, {job}")
        jobs = Job.objects.filter(
            Q(title__icontains=job) & Q(location__icontains=location)
        )
        return render(
            request,
            "index.html",
            {
                "jobs": jobs,
            },
        )


class CompanyPageView(LoginRequiredMixin, CreateView):
    template_name = "company.html"
    context_object_name = "form"
    model = User
    form_class = CompanyForm
    success_url = reverse_lazy("home:home")

    def form_valid(self, form):

        user = get_object_or_404(User, email=self.request.user.email)
        setUser = form.save(commit=False)
        setUser.user = user
        setUser.save()

        return super(CompanyPageView, self).form_valid(form)
