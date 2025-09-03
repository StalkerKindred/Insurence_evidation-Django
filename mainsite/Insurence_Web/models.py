from django.db import models

# Create your models here.
class InsuredPersons(models.Model):
        #insured_id = 
        #insurer_person = 
        name = models.CharField(max_length=40)
        age = models.IntegerField()
        phone_number = models.IntegerField()
        email = models.CharField(max_length=100)
        #password = 

class InsurerPersons(models.Model):
        #insurer_id = 
        name = models.CharField(max_length=40)
        email = models.CharField(max_length=100)
        #password = 

class InsurenceQuestionare(models.Model):
        #Default 0 means No
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

class Insurence(models.Model):
        insured_person = models.ForeignKey(InsuredPersons, on_delete=models.CASCADE)
        insurer_person = models.ForeignKey(InsurerPersons, on_delete=models.CASCADE)
        Insurence_questionare = models.ForeignKey(InsurenceQuestionare, on_delete=models.CASCADE)
        insurence_start = models.DateTimeField()
        insurence_end = models.DateTimeField()
        insurence_type = models.CharField(max_length=100)
        insurence_monthly_payment = models.IntegerField()
        insurence_loss_payment = models.IntegerField()
