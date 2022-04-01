from unittest import result
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse

from .forms import ApplicantForm
from .models import Applicants 
from .serializers import ApplicantsSerializers

from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response 
from rest_framework import status
from django.templatetags.static import static

import pickle
import json 
import numpy as np 
import pandas as pd 
import sklearn
import os 

cwd = os.getcwd()

class ApplicantsView(viewsets.ModelViewSet):
    queryset = Applicants.objects.all()
    serializer_class = ApplicantsSerializers

# Create your views here.
def status(features, ml_model, transformer):
    try:
        cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed','ApplicantIncome', 'CoapplicantIncome', 'LoanAmount','Loan_Amount_Term', 'Credit_History','Property_Area']
        
        df = pd.DataFrame(data = np.array(features).reshape(1,-1), columns = cols)
        
        x_transform = transformer.transform(df)
        y_pred  = ml_model.predict(x_transform) 

        if y_pred == 1:
            result = "Yes" 
        else: 
            result = "No"
        return result
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def index(request):
    return render(request, "loanprediction/index.html")

def form(request):
    if request.method == "POST":
        form = ApplicantForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            marital_status = form.cleaned_data['marital_status']
            dependents = form.cleaned_data['dependents']
            education = form.cleaned_data["education"]
            employment = form.cleaned_data["employment"]
            applicantincome = int(form.cleaned_data["income"])
            coapplicantincome = float(form.cleaned_data["coapplicant"])
            loanamount = float(form.cleaned_data["amount"])
            loanterm = float(form.cleaned_data["loan_term"])
            credit_history = (form.cleaned_data["credit_history"])
            property_area = form.cleaned_data["property_area"]

            input_features = [gender, marital_status, dependents, education, employment , applicantincome, coapplicantincome, loanamount, loanterm, credit_history, property_area]
            model = pickle.load(open(os.path.join(cwd, "loanprediction","model.sav"), 'rb'))
            col_transformer = pickle.load(open(os.path.join(cwd,"loanprediction","column_transformer.p"),'rb'))            
            print(input_features)
            
            result = status(features = input_features, ml_model= model, transformer=col_transformer)
            print(result)
            
            return render(request, "loanprediction/result.html", {
                "result": result,
                "name": form.cleaned_data["firstname"]
            })
        else:
            return render(request, "loanprediction/form.html", {
                "form": form
            })
    return render(request,"loanprediction/form.html", {
        "form": ApplicantForm()
    })


