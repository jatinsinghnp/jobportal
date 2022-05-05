from django import forms
from job.models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = (
            "phone",
            "gender",
            "type",
            "status",
            "company_name",
        )
