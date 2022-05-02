from django.db import models
from accounts.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

GENDER = [
    ("Male", "Male"),
    ("female", "female"),
    ("others", "others"),
]


class Applicant(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="")
    gender = models.CharField(max_length=50, choices=GENDER)
    type = models.CharField(max_length=15)

    def __str__(self):
        return self.user.first_name


STATUS = [
    ("pending", "pending"),
    ("active", "active"),
]


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="")
    gender = models.CharField(max_length=50, choices=GENDER)
    type = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=STATUS)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Job(models.Model):
    CHOICES = [
        ("FullTime", "FullTime"),
        ("PartTime", "PartTime"),
    ]
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=200)
    salary = models.FloatField()
    image = models.ImageField(upload_to="")
    description = models.TextField(max_length=400)
    experience = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    types = models.CharField(max_length=300, choices=CHOICES)
    creation_date = models.DateField()

    def __str__(self):
        return self.title
    


class Application(models.Model):
    company = models.CharField(max_length=200, default="")
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    resume = models.ImageField(upload_to="")
    apply_date = models.DateField()

    def __str__(self):
        return str(self.applicant)


