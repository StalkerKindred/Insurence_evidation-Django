from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import InsuredForm, QuestionareForm, InsurenceForm
from .models import InsuredPersons #InsurerEmployees, Insurence, InsurenceQuestionare

#Right side menus:
#Use : {"right_side_menu": utility_menu}
UTILITY_MENU = "Insurence_Web/right_side_menu_utilities.html"
#Use : {"right_side_menu": flavor_text_menu}
FLAVOR_TEXT_MENU = 'Insurence_Web/right_side_menu.html'

SEARCH_LOOKUP_TYPE = "__icontains"

#-------------------------------------------------------------------------
#---------------------------Functions for views---------------------------
#-------------------------------------------------------------------------

def get_fields_search(model):
    search_fields = []
    for field in model._meta.fields:
        if field.get_internal_type() in ["CharField", "TextField"]:
            search_fields.append((field.name, f"{SEARCH_LOOKUP_TYPE}"))
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

def get_all_model_instances(model):
    """Returns all objects of a model given"""
    models = model.objects.all()
    return models

#-----------------------------------------------------------
#---------------------------Views---------------------------
#-----------------------------------------------------------

def insured_profile(request, id):
    """View for insured profile."""
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

    return render(request,
                  "Insurence_Web/insured/insured_profile_card.html", 
                        {
                            "title": title,
                            "person_json_info": person_json_info,
                            "picture": picture_path,
                            "right_side_menu": FLAVOR_TEXT_MENU
                                                                }
                                                                    )

def index(request):
    """View for basic home page."""
    context = "Placeholder Home Page Text"
    return render(request,
                  "Insurence_Web/home/home.html",
                        {
                            "message": context,
                            "right_side_menu": FLAVOR_TEXT_MENU
                                                                }
                                                                    )

def index_updates(request):
    """View for viewing new updates to this application"""
    context = "Placeholder Update"
    return render(request,
                  "Insurence_Web/home/updates.html",
                        {
                            "message": context,
                            "right_side_menu": FLAVOR_TEXT_MENU
                                                                }
                                                                    )

    # - Insured
def insured_new(request):
    """View creating new insured object"""
    title = "New Insured"
    if request.method == "POST":
        form = InsuredForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = InsuredForm()
    return render(request,
                  "Insurence_Web/form.html",
                  {
                    "form": form,
                    "title": title, 
                    "right_side_menu": FLAVOR_TEXT_MENU
                                                        }
                                                            )

def insured_search(request):
    """View with search function returning back found objects"""
    title = 'Searching'

    payload = {"title": title,
                "right_side_menu": UTILITY_MENU}

    query = request.GET.get("q")

    if query:
        payload['query'] = query

        searching_results = InsuredPersons.objects.filter(
            Q(insured_id__icontains=query)
            | Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(state__icontains=query)
            | Q(city__icontains=query)
            | Q(phone_number__icontains=query)
            | Q(email__icontains=query)
        )

        if searching_results.exists():
            data_payload = {}
            person_count = 0
            for person in searching_results:
                data_payload[person.get_id()] = person.searching_results_dict()
                person_count += 1

            payload['search_result_data'] = data_payload

            button_count = person_count / 12

            if button_count >= 1:
                if isinstance(button_count, float):
                    button_count = int(button_count) + 1
                button_range = (1, button_count)
                payload['button_range'] = button_range

        else:
            message = f'Searching for person with "{query}" did not find anyone.'
            payload['error_message'] = message

    return render(request, 'Insurence_Web/searching.html', payload)

    # - Insurences
def insurence_new(request):
    """View creating new insurence forms"""
    title = "New Insurence"
    if request.method == "POST":
        form = InsurenceForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = InsurenceForm()
    return render(request,
                  "Insurence_Web/form.html", 
                  {
                    "form": form,
                    "title": title, 
                    "right_side_menu": FLAVOR_TEXT_MENU
                                                        }
                                                            )

#def insurence_my():

#def insurence_search():

    # - Questionares
def questionare_new(request):
    """View creating new questionares forms"""
    title = "New Questionare"
    if request.method == "POST":
        form = QuestionareForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QuestionareForm()
    return render(request,
                    "Insurence_Web/form.html",
                        {
                            "form": form,
                            "title": title, 
                            "right_side_menu": FLAVOR_TEXT_MENU
                                                                }
                                                                    )
