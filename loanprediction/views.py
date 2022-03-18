from django.shortcuts import render
from django import forms

gender_choices = (("","-- Select gender --"), ("Male","male"), ("Female","female"))
marital_choices = (("", "-- Select marital status --"), ("Yes", "married"), ("No", "not married"))
dependents_choices = (("", "-- Number of dependents --"), ("0","None"), ("1", "One"), ("2", "Two"), ("3+", "More than two"))
education_choices = (("", "-- Are you a graduate --"), ("Graduate", "Yes"), ("Not Graduate","No"))
employment_choices = (("", "-- Are you self-employed --"), ("Yes", "Yes"), ("No", "No"))
credit_choices = (("", "-- Do you have an outstanding unpaid loan --"), ("1.0", "Yes"), ("0.0","No"))
property_choices = (("", "-- Property area --"), ("Urban","Urban"), ("Semiurban","Semi-Urban"), ("Rural", "Rural"))


class LoanFeatures(forms.Form):
    gender = forms.ChoiceField(label = "Gender", choices = gender_choices, widget=forms.Select(attrs={'class':"form-select form-select-lg mb-3"}))
    marital_status = forms.ChoiceField(label = "Marital status", choices = marital_choices, widget = forms.Select(attrs = {'class':"form-select form-select-lg mb-3"}))
    dependents = forms.ChoiceField(label = "Dependents", choices = dependents_choices, widget = forms.Select(attrs = {'class':"form-select form-select-lg mb-3"}))
    education = forms.ChoiceField(label = "Education", choices = education_choices, widget= forms.Select(attrs = {'class': "form-select form-select-lg mb-3"}))
    employment = forms.ChoiceField(label = "Employment", choices = employment_choices, widget = forms.Select(attrs = {'class':"form-select form-select-lg mb-3"}))
    credit_history = forms.ChoiceField(label = "Credit History", choices = credit_choices, widget = forms.Select(attrs = {'class':"form-select form-select-lg mb-3"}))
    property_area = forms.ChoiceField(label = "Property Area", choices = property_choices, widget = forms.Select(attrs = {'class':"form-select form-select-lg mb-3"}))
    income = forms.IntegerField(label = "Income", min_value=2, widget = forms.TextInput(attrs = {'class': "form-select form-select-lg mb-3"}))
    coapplicant = forms.IntegerField(label = "Coapplicant's Income", widget = forms.TextInput(attrs = {'class':"form-select form-select-lg mb-3"}))
    amount = forms.IntegerField(label = "Loan Amount", widget = forms.TextInput(attrs = {'class': "form-select form-select-lg mb-3"}))
    loan_term = forms.IntegerField(label = "Loan_term", widget = forms.TextInput(attrs = {'class': "form-select form-select-lg mb-3"}))

# Create your views here.
def index(request):
    return render(request, "loanprediction/index.html")

def form(request):
    clean_features = []
    if request.method == "POST":
        form = LoanFeatures(request.POST)
        if form.is_valid():
            features = ['gender','marital_status','dependents','education','employment','credit_history','property_area','income','coapplicant','amount','loan_term']
            for feat in features:
                clean_features.append(form.cleaned_data[feat])

    return render(request,"loanprediction/form.html", {
        "form": LoanFeatures()
    })
