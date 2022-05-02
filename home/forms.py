from django import forms
from job.models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields = "__all__"
        



