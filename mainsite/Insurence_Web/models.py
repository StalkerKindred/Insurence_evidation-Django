from django.db import models

# Create your models here.
#Passwords will be stored as imprints that will be encoded

class InsurerEmployees(models.Model):
        #Keys
        insurer_id = models.PositiveIntegerField(primary_key=True)
        #Data
        first_name = models.CharField(max_length=40)
        last_name = models.CharField(max_length=40)
        email = models.CharField(max_length=100)
        password = models.CharField(max_length=100)

        def __str__(self):
                return  self.first_name + f" {self.last_name}" + f" - ID: {self.insurer_id}"
        
        def contacts(self):
                return (f"Email: {self.email}")
        
class InsuredPersons(models.Model):
        #Keys
        insured_id = models.PositiveIntegerField(primary_key=True)
        insurer = models.ForeignKey(InsurerEmployees, on_delete=models.PROTECT)
        #Data
        first_name = models.CharField(max_length=40)
        last_name = models.CharField(max_length=40)
        date_of_birth = models.PositiveIntegerField()
        phone_number = models.PositiveIntegerField()
        email = models.CharField(max_length=100)
        password = models.CharField(max_length=100) 

        def __str__(self):
                return  self.first_name + f" {self.last_name}" + f" - ID: {self.insured_id}"
        
        def contacts(self):
                return (f"""Email: {self.email}
                        Phone: {self.phone_number}""")
        
class InsurenceQuestionare(models.Model):
        #Keys
        insurence_questionare_id = models.PositiveIntegerField(primary_key=True)
        insured = models.ForeignKey(InsuredPersons, on_delete=models.CASCADE, related_name="insured_person")
        insurer = models.ForeignKey(InsuredPersons, on_delete=models.PROTECT, related_name="insurer_employee")
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
        insurence_monthly_payment = models.PositiveIntegerField()
        insurence_claims_payment = models.PositiveIntegerField()

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