from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import *
from django.db.models import Q
from .models import InsuredPersons, InsurerEmployees, Insurence, InsurenceQuestionare

#Right side menus:
#Use : {"right_side_menu": utility_menu}
utility_menu = "Insurence_Web/right_side_menu_utilities.html"
#Use : {"right_side_menu": flavor_text_menu}
flavor_text_menu = 'Insurence_Web/right_side_menu.html'

search_lookup_type = "__icontains"

#-------------------------------------------------------------------------
#---------------------------Functions for views---------------------------
#-------------------------------------------------------------------------

def get_fields_search(model):
    search_fields = []
    for field in model._meta.fields:
        if field.get_internal_type() in ["CharField", "TextField"]:
                search_fields.append((field.name, f"{search_lookup_type}"))
        elif field.get_internal_type() in ["IntegerField"]:
                search_fields.append((field.name, ""))
    return search_fields

def get_fields(model):
    return [field.name for field in model._meta.fields]

def get_field_data(fields, instance):
    data = []
    for field in fields:
        data.append(getattr(instance, field))
    return data

#-----------------------------------------------------------
#---------------------------Views---------------------------
#-----------------------------------------------------------

def insured_profile(request, id):
    person = get_object_or_404(InsuredPersons, pk=id)

    picture_path = ""

    gender = person.get_gender()

    if gender == "Male":
        picture_path = "images/male_icon.png"
    elif gender == "Female":
        picture_path = "images/female_icon.png"
    else:
        picture_path = "images/unspecified_gender_icon.png"

    person_json_info =  person.information_to_json()

    title = person_json_info["Personal_info"]["Name"]

    return render(request, "Insurence_Web/insured/insured_profile_card.html", {"title": title,
                                                                                "person_json_info": person_json_info,
                                                                               "picture": picture_path,
                                                                               })

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
    return render(request, "Insurence_Web/home/home.html",  {"message": context, 
                                                             "right_side_menu": flavor_text_menu})

def index_updates(request):
    context = "Placeholder Update" 
    return render(request, "Insurence_Web/home/updates.html",  {"message": context, 
                                                                "right_side_menu": flavor_text_menu})

    # - Insured 
def insured_new(request):
    title = "New Insured"
    if request.method == "POST":
        form = InsuredForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = InsuredForm()
    return render(request, "Insurence_Web/form.html", {"form": form, 
                                                        "title": title, 
                                                        "right_side_menu": flavor_text_menu})

def insured_search(request):
    title = 'Searching'
    query = request.GET.get("q")
    options = []
    
    if query:
        searching_results = InsuredPersons.objects.all()
        search_fields = get_fields_search(InsuredPersons)

            # Fix ak to najde personu nech ju to len skipne
        for word in query.split():
            q_object = Q()
            for field_name, lookup in search_fields:
                if lookup:
                    q_object |= Q(**{f"{field_name}{lookup}": word})
                elif word.isdigit():
                    q_object |= Q(**{field_name: int(word)})

                searching_results = searching_results.filter(q_object)

        return render(request, 'Insurence_Web/searching.html', {"title": title, 
                                                                 "right_side_menu": utility_menu, 
                                                                 'search_result_list': searching_results
                                                                 })
    
    return render(request, 'Insurence_Web/searching.html', {"title": title, 
                                                             "right_side_menu": utility_menu})

    # - Insurences
def insurence_new(request):
    title = "New Insurence"
    if request.method == "POST":
        form = InsurenceForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = InsurenceForm()
    return render(request, "Insurence_Web/form.html", {"form": form, 
                                                       "title": title, 
                                                       "right_side_menu": flavor_text_menu})

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
    return render(request, "Insurence_Web/form.html", {"form": form , 
                                                       "title": title, 
                                                       "right_side_menu": flavor_text_menu})
"""  
def questionare_search():

    # - Account
def account_profile():

def account_settings():

def account_sign_out():
"""