from django.db import models
from django.conf import settings


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    ceo = models.CharField(max_length=100)
    established = models.DateField()
    industry_type = models.CharField(max_length=50)
    criteria = models.DecimalField(max_digits=4, decimal_places=2)
    is_core = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    placed_year = models.IntegerField()
    course = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    package = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.student_name


class Queries(models.Model):
    query = models.CharField(max_length=200)
    response = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.query
