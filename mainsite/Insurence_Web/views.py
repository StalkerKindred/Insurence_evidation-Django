from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import InsuredPersons, InsurerEmployees, Insurence, InsurenceQuestionare

def index(request):
    context = "This is truly the begining" 
    return render(request, "Insurence_Web/base.html", {"message": context})

def insured_detail(request, id):
    detail = get_object_or_404(InsuredPersons, pk=id)
    return HttpResponse(str(detail) +" "+ detail.contacts())

def insurence_detail(request, id):
    detail = get_object_or_404(Insurence, pk=id)
    return HttpResponse(str(detail) + " "+ detail.more_info() + " " + detail.payments())

def questionare_detail(request, id):
    detail = get_object_or_404(InsurenceQuestionare, pk=id)
    return HttpResponse(detail.more_info())
