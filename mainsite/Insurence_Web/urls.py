from django.urls import path

from .models import InsuredPersons

from . import views

urlpatterns = [
    # - home
    path("", views.index, name="Index"),
    path("Home", views.index, name="Index"),
    path("Home/Updates", views.index_updates, name="Updates"),
    #Insured things
    path("Insured/New", views.insured_new, name="Insured New"),
    path("Insured/Searching", views.search, {"model": InsuredPersons}, name="Insured Searching"),
    #path("insured/searching/{sql bs}", views.insured_new, name="insured new"),
    path("Insured/Profile/<int:model_id>", views.insured_profile, name="Insured Profile"),
    #Insurence things
    path("Insurence/New", views.insurence_new, name="Insurence New"),
    #Questionare things
    path("Questionare/New", views.questionare_new, name="Questionare New")
]
