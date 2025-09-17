from django.shortcuts import render
from django.http import HttpResponse
from .models import InsuredPersons, InsurerEmployees, Insurence, InsurenceQuestionare
def index(request):
    return HttpResponse("This is the begining")

def insured_detail(request, id):
    detail = InsuredPersons.objects.get(insured_id=id)
    return HttpResponse(str(detail) +" "+ detail.contacts())

def insurence_detail(request, id):
    detail = Insurence.objects.get(insurence_id=id)
    return HttpResponse(str(detail) + " "+ detail.more_info() + " " + detail.payments())

def questionare_detail(request, id):
    detail = InsurenceQuestionare.objects.get(insurence_questionare_id=id)
    return HttpResponse(detail.more_info())
