from rest_framework import serializers 
from .models import Applicants

class ApplicantsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Applicants
        fields = "__all__"