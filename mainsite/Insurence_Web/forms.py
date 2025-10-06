from django import forms
from .models import InsuredPersons, Insurence, InsurenceQuestionare

class InsuredForm(forms.ModelForm):
    class Meta:
        model = InsuredPersons
        fields = [  #Keys
                    "insured_id",
                    #Data
                    "first_name",
                    "last_name",
                    "gender",
                    "date_of_birth",
                    "phone_number",
                    "email"
                    ]
        
        widgets = { #Keys
                    "insured_id": forms.TextInput(attrs={"class":"form-control"}),
                    #Data
                    "first_name": forms.TextInput(attrs={"class":"form-control"}),
                    "last_name": forms.TextInput(attrs={"class":"form-control"}),
                    "gender": forms.Select(attrs={"class":"form-control"}),
                    "date_of_birth": forms.TextInput(attrs={"class":"form-control"}),
                    "phone_number": forms.TextInput(attrs={"class":"form-control"}),
                    "email": forms.TextInput(attrs={"class":"form-control"})
                    }
        
class InsurenceForm(forms.ModelForm):
    class Meta:
        model = Insurence
        fields = [  #Keys
                    "insurence_id",
                    "insured",
                    "insurer",
                    "insurence_questionare",
                    #Data
                    "insurence_start",
                    "insurence_end",
                    "insurence_type",
                    "insurence_monthly_payment",
                    "insurence_claims_payment"
                    ]
        
        widgets = { #Keys
                    "insurence_id": forms.TextInput(attrs={"class":"form-control"}),
                    "insured": forms.Select(attrs={"class":"form-control"}),
                    "insurer": forms.Select(attrs={"class":"form-control"}),
                    "insurence_questionare": forms.Select(attrs={"class":"form-control"}),
                    #Data
                    "insurence_start": forms.TextInput(attrs={"class":"form-control"}),
                    "insurence_end": forms.TextInput(attrs={"class":"form-control"}),
                    "insurence_type": forms.TextInput(attrs={"class":"form-control"}),
                    "insurence_monthly_payment": forms.TextInput(attrs={"class":"form-control"}),
                    "insurence_claims_payment": forms.TextInput(attrs={"class":"form-control"})
                    }
        
class QuestionareForm(forms.ModelForm):
    class Meta:
        model = InsurenceQuestionare
        fields = [  #Keys
                    "insurence_questionare_id",
                    "insured",
                    "insurer",
                    #Data
                    "question_1_answer",
                    "question_2_answer",
                    "question_3_answer",
                    "question_4_answer",
                    "question_5_answer",
                    "question_6_answer",
                    "question_7_answer",
                    "question_8_answer",
                    "question_9_answer",
                    "question_10_answer"
                    ]
        
        widgets = { #Keys
                    "insurence_questionare_id": forms.TextInput(attrs={"class":"form-control"}),
                    "insured": forms.Select(attrs={"class":"form-control"}),
                    "insurer": forms.Select(attrs={"class":"form-control"}),
                    #Data
                    "question_1_answer": forms.TextInput(attrs={"class":"form-control"}),
                    "question_2_answer": forms.TextInput(attrs={"class":"form-control"}),
                    "question_3_answer": forms.TextInput(attrs={"class":"form-control"}),
                    "question_4_answer": forms.TextInput(attrs={"class":"form-control"}),
                    "question_5_answer": forms.TextInput(attrs={"class":"form-control"}),
                    "question_6_answer": forms.TextInput(attrs={"class":"form-control"}),
                    "question_7_answer": forms.TextInput(attrs={"class":"form-control"}),
                    "question_8_answer": forms.TextInput(attrs={"class":"form-control"}),
                    "question_9_answer": forms.TextInput(attrs={"class":"form-control"}),
                    "question_10_answer": forms.TextInput(attrs={"class":"form-control"})
                    }

