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

#Redundant
def get_fields_search(model):
    search_fields = []
    model_fields = model.field_names_for_searching()
    for field in model_fields["text_field"]:
        search_fields.append((field + f"{SEARCH_LOOKUP_TYPE}"))
    for field in model_fields["integer_field"]:
        search_fields.append((field + f"{SEARCH_LOOKUP_TYPE}"))
    return search_fields

#------------------------------------------------------------------------
#---------------------------Views----------------------------------------
#------------------------------------------------------------------------

def insured_profile(request, model_id):
    """View for insured profile."""
    person = get_object_or_404(InsuredPersons, pk=model_id)

    picture_path = ""

    gender = person.get_gender()

    if gender == "Male":
        picture_path = "images/male_icon.png"
    elif gender == "Female":
        picture_path = "images/female_icon.png"
    else:
        picture_path = "images/unspecified_gender_icon.png"

    person_json_info =  person.information_for_profile_to_json()

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

def search(request, model=None):
    """View with search function returning back found objects of a model"""
    title = 'Searching'

    payload = {"title": title,
                "right_side_menu": UTILITY_MENU}

    query = request.GET.get("q")

    show_all = request.GET.get("all")

    if query or show_all:
        payload['query'] = query

        fields = get_fields_search(model)

        if query:     
            q = Q()
            for field_name in fields:
                q |= Q(**{field_name: query})
            searching_results = model.objects.filter(q)
        else:
            searching_results = model.objects.all()

        if searching_results.exists():
            data_payload = {}
            item_count = 0

            #Getting fields for view
            object_table_fields = []
            for key in searching_results[0].searching_results_data():
                object_table_fields.append(key)

            payload['search_result_fields'] = object_table_fields
            #Getting Data and their fields for view
            for item in searching_results:
                data_payload[item.get_id()] = item.searching_results_data()
                item_count += 1

            payload['search_result_data'] = data_payload

            button_count = item_count / 12

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
