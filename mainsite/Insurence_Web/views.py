from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import InsuredPersons, InsurerEmployees, Insurence, InsurenceQuestionare

def insured_detail(request, id):
    detail = get_object_or_404(InsuredPersons, pk=id)
    return HttpResponse(str(detail) +" "+ detail.contacts())

def insurence_detail(request, id):
    detail = get_object_or_404(Insurence, pk=id)
    return HttpResponse(str(detail) + " "+ detail.more_info() + " " + detail.payments())

def questionare_detail(request, id):
    detail = get_object_or_404(InsurenceQuestionare, pk=id)
    return HttpResponse(detail.more_info())

# - views for menu
    # - Home

def index(request):
    context = "Placeholder text lorem ipsum bla bla." 
    return render(request, "Insurence_Web/home/home.html",  {"message": context})

def index_updates(request):
    context = "Placeholder Update text lorem ipsum bla bla." 
    return render(request, "Insurence_Web/home/updates.html",  {"message": context})
"""
    # - Insured 
def insured_new():

def insured_search():

    # - Insurences
def insurence_new():

def insurence_my():

def insurence_search():

    # - Questionares
def questionare_new():

def questionare_search():

    # - Account
def account_profile():

def account_settings():

def account_sign_out():
"""