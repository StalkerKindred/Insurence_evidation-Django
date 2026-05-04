from django.db import models

from datetime import date

# from phonenumbers.phonenumberutil import COUNTRY_CODE_TO_REGION_CODE
from phonenumbers import phonenumberutil as pnu # import COUNTRY_CODE_TO_REGION_CODE


def country_code_to_prefix(country_code):
       return str(pnu.country_code_for_valid_region(country_code))

def get_prefix_choices():
    choices = []

    for code, regions in pnu.COUNTRY_CODE_TO_REGION_CODE.items():
        for region in regions:
            if region == "001":  # skip non-geographic
                continue
            choice = [region, f"{region} +{code}"]
            choices.append(choice)

    choices.sort(key=lambda x: x[0])

    return choices

#Passwords will be later stored as imprints that will be encoded

#Choices:
gender_choices = [
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other"),
        ]
        


prefix_number_choices = get_prefix_choices()
#Models
class InsurerEmployees(models.Model):
        #Keys
        insurer_id = models.PositiveIntegerField(primary_key=True)
        #Data
        first_name = models.CharField(max_length=40)
        last_name = models.CharField(max_length=40)
        gender = models.CharField(max_length=7, choices=gender_choices, default="M")
        #Contacts
        email = models.EmailField()
        phone_number_prefix = models.CharField(max_length=4, choices=prefix_number_choices, default="CZ")
        phone_number = models.IntegerField()
        #Else
        password = models.CharField(max_length=100)

        def __str__(self):
                return  self.first_name + f" {self.last_name}" + f" - ID: {self.insurer_id}"
        
        def contacts(self):
                return (f"Email: {self.email}")
        
class InsuredPersons(models.Model):
        #Keys
        insured_id = models.PositiveIntegerField(primary_key=True)
        #Data
        #Personal info
        first_name = models.CharField(max_length=40)
        last_name = models.CharField(max_length=40)
        gender = models.CharField(max_length=7, choices=gender_choices, default="Other")
        date_of_birth = models.DateField()
        birth_number = models.IntegerField()
        goverment_id = models.CharField(max_length=8)
        #Address
        state = models.CharField(max_length=40)
        city = models.CharField(max_length=40)
        parcel = models.CharField(max_length=40)
        home_number = models.IntegerField()
        home_delivery_number = models.IntegerField()
        post_code = models.IntegerField()
        #Bank Info
        bank_account_number = models.IntegerField()
        #Contact
        phone_number_prefix = models.CharField(max_length=4, choices=prefix_number_choices, default="CZ")
        phone_number = models.IntegerField()
        email = models.EmailField()
        
        def get_age(self):
                today = date.today()
                age = today.year - self.date_of_birth.year

                if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
                        age -= 1

                return age
        
        # Functions for View

        def get_gender(self):
                return self.gender

        def get_id(self):
               return self.insured_id

        def __str__(self):
                return  self.first_name + f" {self.last_name}"
        
        def information_to_json(self):
                results = {'Personal_info' : {'Name' : f'{self.first_name + ' ' + self.last_name}',
                                                'Age' : f'{self.get_age()}',
                                                'Gender' : self.gender},
                                'Contacts' : {'Phone' : f'+{str(country_code_to_prefix(self.phone_number_prefix) + str(self.phone_number))}',
                                              'Email' : self.email},
                                'Address' : {'State' : self.state,
                                            'City' : self.city,
                                            'Parcel' : self.parcel,
                                            'Home Number' : f'{str(self.home_number) + '/' + str(self.home_delivery_number)}' },
                                            'Postal Code' : self.post_code
                                                }

                return results
        
        #Function solely for searching.html so that its less of a hassle to work with it
        def information_to_json_searching_results(self):
                results = {
                                'Name' : f'{self.first_name + ' ' + self.last_name}',
                                'Birth' : self.date_of_birth,
                                'City' : self.city,
                                'Phone' :f'+{str(country_code_to_prefix(self.phone_number_prefix) + str(self.phone_number))}',
                                'Email' : self.email
                                                        }

                return results






class InsurenceQuestionare(models.Model):
        #Keys
        insurence_questionare_id = models.PositiveIntegerField(primary_key=True)
        insured = models.ForeignKey(InsuredPersons, on_delete=models.CASCADE, related_name="insured_person")
        insurer = models.ForeignKey(InsurerEmployees, on_delete=models.PROTECT, related_name="insurer_employee")
        #Default 0 means No
        #Data
        question_1_answer = models.IntegerField(default=0)
        question_2_answer = models.IntegerField(default=0)
        question_3_answer = models.IntegerField(default=0)
        question_4_answer = models.IntegerField(default=0)
        question_5_answer = models.IntegerField(default=0)
        question_6_answer = models.IntegerField(default=0)
        question_7_answer = models.IntegerField(default=0)
        question_8_answer = models.IntegerField(default=0)
        question_9_answer = models.IntegerField(default=0)
        question_10_answer = models.IntegerField(default=0)

        def __str__(self):
                return (f"Insurence Questionare ID: {self.insurence_questionare_id}")
        
        def more_info(self):
                return (f"""Insurence Questionare ID: {self.insurence_questionare_id} 
                        Filled by {self.insured}
                        Signed by {self.insurer}""")
        
class Insurence(models.Model):
        #Keys
        insurence_id = models.PositiveIntegerField(primary_key=True)
        insured = models.ForeignKey(InsuredPersons, on_delete=models.CASCADE)
        insurer = models.ForeignKey(InsurerEmployees, on_delete=models.CASCADE)
        insurence_questionare = models.ForeignKey(InsurenceQuestionare, on_delete=models.CASCADE)
        #Data
        insurence_start = models.DateTimeField()
        insurence_end = models.DateTimeField()
        insurence_type = models.CharField(max_length=100)
        insurence_monthly_payment = models.FloatField()
        insurence_claims_payment = models.FloatField()

        def __str__(self):
                return (f"Insurence ID: {self.insurence_id}")
        
        def more_info(self):
                return (f"""Insurence  ID: {self.insurence_id} 
                        Insurence Type {self.insurence_type}
                        Filled by {self.insured}
                        Signed by {self.insurer}""")
        
        def payments(self):
                return(f"""Start {self.insurence_start}
                        End {self.insurence_end}
                        Monthly Payment {self.insurence_monthly_payment}
                        Claims Payment {self.insurence_claims_payment}""")