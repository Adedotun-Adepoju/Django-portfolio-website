from django.db import models

# Create your models here.
class Applicants(models.Model):
    gender = models.CharField(max_length = 16)
    marital_status = models.CharField(max_length = 16)
    Dependents = models.CharField(max_length = 16)
    Education = models.CharField(max_length = 16)
    Employment = models.CharField(max_length = 16)
    credit_history = models.CharField(max_length = 16)
    property_area = models.CharField(max_length = 16)
    Income = models.IntegerField()
    Coapplicant_income = models.IntegerField()
    Loan_Amount = models.IntegerField()
    Loan_term = models.IntegerField()
    Approved = models.CharField(max_length = 16)

    def __str__(self):
        return f"{self.id}"

