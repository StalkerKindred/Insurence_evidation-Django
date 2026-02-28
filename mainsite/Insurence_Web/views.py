from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import InsuredPersons, InsurerEmployees, Insurence, InsurenceQuestionare

#Right side menus:
#Use : {"right_side_menu": utility_menu}
utility_menu = "Insurence_Web/right_side_menu_utilities.html"
#Use : {"right_side_menu": flavor_text_menu}
flavor_text_menu = 'Insurence_Web/right_side_menu.html'



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
    context = "Placeholder Home Page Text" 
    return render(request, "Insurence_Web/home/home.html",  {"message": context, "right_side_menu": flavor_text_menu})

def index_updates(request):
    context = "Placeholder Update" 
    return render(request, "Insurence_Web/home/updates.html",  {"message": context, "right_side_menu": flavor_text_menu})

    # - Insured 
def insured_new(request):
    title = "New Insured"
    if request.method == "POST":
        form = InsuredForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = InsuredForm()
    return render(request, "Insurence_Web/form.html", {"form": form, "title": title, "right_side_menu": flavor_text_menu})

def insured_search(request):
    title = 'Searching'
    options = []
    
    return render(request, f'Insurence_Web/searching.html', {"title": title, "right_side_menu": utility_menu})

    # - Insurences
def insurence_new(request):
    title = "New Insurence"
    if request.method == "POST":
        form = InsurenceForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = InsurenceForm()
    return render(request, "Insurence_Web/form.html", {"form": form, "title": title, "right_side_menu": flavor_text_menu})

#def insurence_my():

#def insurence_search():

    # - Questionares
def questionare_new(request):
    title = "New Questionare"
    if request.method == "POST":
        form = QuestionareForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QuestionareForm()
    return render(request, "Insurence_Web/form.html", {"form": form , "title": title, "right_side_menu": flavor_text_menu})
"""  
def questionare_search():

    # - Account
def account_profile():

def account_settings():

def account_sign_out():
"""