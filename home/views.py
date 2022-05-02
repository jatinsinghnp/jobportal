from django.shortcuts import render
from django.views.generic import ListView
from job.models import Job
from django.db.models import Q
from django.views.generic import CreateView
from job.models import Company
from home.forms import CompanyForm
from django.contrib import messages


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


class CompanyPageView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = "a.html"

    def form_valid(self, form):
        messages.success("save sucess fully")
        return super().form_valid(form)
