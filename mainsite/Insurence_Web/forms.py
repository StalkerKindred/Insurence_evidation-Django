from django import forms
from .models import InsuredPersons

class InsuredForm(forms.ModelForm):
    class Meta:
        model = InsuredPersons
        fields = [#Keys
                    "insured_id",
                    #Data
                    "first_name",
                    "last_name",
                    "gender",
                    "date_of_birth",
                    "phone_number",
                    "email"
                    ]
        
        widgets = {  #Keys
                    "insured_id": forms.TextInput(attrs={"class":"form-control"}),
                    #Data
                    "first_name": forms.TextInput(attrs={"class":"form-control"}),
                    "last_name": forms.TextInput(attrs={"class":"form-control"}),
                    "gender": forms.Select(attrs={"class":"form-control"}),
                    "date_of_birth": forms.TextInput(attrs={"class":"form-control"}),
                    "phone_number": forms.TextInput(attrs={"class":"form-control"}),
                    "email": forms.TextInput(attrs={"class":"form-control"})
                    }

