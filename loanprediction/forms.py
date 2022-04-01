from django import forms 
from .models import Applicants 

gender_choices = (("","-- Select gender --"), ("Male","Male"), ("Female","Female"))
marital_choices = (("", "-- Select marital status --"), ("Yes", "Married"), ("No", "Not married"))
dependents_choices = (("", "-- Number of dependents --"), ("0","None"), ("1", "One"), ("2", "Two"), ("3+", "More than two"))
education_choices = (("", "-- Are you a graduate --"), ("Graduate", "Yes"), ("Not Graduate","No"))
employment_choices = (("", "-- Are you self-employed --"), ("Yes", "Yes"), ("No", "No"))
credit_choices = (("", "-- Do you have an outstanding unpaid loan --"), ("0.0", "Yes"), ("1.0","No"))
property_choices = (("", "-- Property area --"), ("Urban","Urban"), ("Semiurban","Semi-Urban"), ("Rural", "Rural"))

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicants 
        exclude = ("approved",)
    
    #gender = forms.TypedChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')],widget=forms.Select(attrs={'class':"form-select form-select-lg mb-3"}))
    firstname = forms.CharField(label = "First Name", required=True, widget=forms.TextInput(attrs={'class':"form-control"}))
    lastname = forms.CharField(label = "Last Name", required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
    gender = forms.ChoiceField(label = "Gender", choices = gender_choices, widget=forms.Select(attrs={'class':"form-select form-select-lg mb-3"}))
    marital_status = forms.ChoiceField(label = "Marital status", choices = marital_choices, widget = forms.Select(attrs = {'class':"form-select form-select-lg mb-3"}))
    dependents = forms.ChoiceField(label = "Dependents", choices = dependents_choices, widget = forms.Select(attrs = {'class':"form-select form-select-lg mb-3"}))
    education = forms.ChoiceField(label = "Education", choices = education_choices, widget= forms.Select(attrs = {'class': "form-select form-select-lg mb-3"}))
    employment = forms.ChoiceField(label = "Employment", choices = employment_choices, widget = forms.Select(attrs = {'class':"form-select form-select-lg mb-3"}))
    credit_history = forms.ChoiceField(label = "Credit History", choices = credit_choices, widget = forms.Select(attrs = {'class':"form-select form-select-lg mb-3"}))
    property_area = forms.ChoiceField(label = "Property Area", choices = property_choices, widget = forms.Select(attrs = {'class':"form-select form-select-lg mb-3"}))
    income = forms.IntegerField(label = "Your Monthly Income in dollars", min_value=2, widget = forms.NumberInput(attrs = {'class': "form-control"}))
    coapplicant = forms.IntegerField(label = "Coapplicant's Income in dollars", widget = forms.NumberInput(attrs = {'class':"form-control"}))
    amount = forms.IntegerField(label = "Loan Amount in dollars", widget = forms.NumberInput(attrs = {'class': "form-control"}))
    loan_term = forms.IntegerField(label = "Loan_term (Number of months to payback)", widget = forms.NumberInput(attrs = {'class': "form-control"}))
