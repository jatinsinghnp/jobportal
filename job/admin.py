from django.contrib import admin
from .models import Applicant, Application, Company, Job, User

# Register your models here.

admin.site.register(Applicant)
admin.site.register(Application)
admin.site.register(Company)
admin.site.register(Job)
