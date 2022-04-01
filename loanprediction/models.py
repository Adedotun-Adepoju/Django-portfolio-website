from django.db import models

gender_choices = (("","-- Select gender --"), ("Male","Male"), ("Female","Female"))
marital_choices = (("", "-- Select marital status --"), ("Yes", "Married"), ("No", "Not married"))
dependents_choices = (("", "-- Number of dependents --"), ("0","None"), ("1", "One"), ("2", "Two"), ("3+", "More than two"))
education_choices = (("", "-- Are you a graduate --"), ("Graduate", "Yes"), ("Not Graduate","No"))
employment_choices = (("", "-- Are you self-employed --"), ("Yes", "Yes"), ("No", "No"))
credit_choices = (("", "-- Do you have an outstanding unpaid loan --"), ("0.0", "Yes"), ("1.0","No"))
property_choices = (("", "-- Property area --"), ("Urban","Urban"), ("Semiurban","Semi-Urban"), ("Rural", "Rural"))

# Create your models here.
class Applicants(models.Model):
    firstname = models.TextField(max_length=20)
    lastname = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length = 16, choices=gender_choices)
    marital_status = models.CharField(max_length = 16, choices=marital_choices)
    dependents = models.CharField(max_length = 16, choices=dependents_choices)
    education = models.CharField(max_length = 16, choices=education_choices)
    employment = models.CharField(max_length = 16, choices=employment_choices)
    credit_history = models.CharField(max_length = 16, choices=credit_choices)
    property_area = models.CharField(max_length = 16, choices=property_choices)
    income = models.IntegerField(default=0)
    coapplicant = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    loan_term = models.IntegerField(default=0)
    approved = models.CharField(max_length = 16)

    def __str__(self):
        return f"{self.id} {self.lastname}"

