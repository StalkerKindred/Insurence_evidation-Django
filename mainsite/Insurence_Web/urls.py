from django.urls import path

from . import views

urlpatterns = [
    # - home
    path("", views.index, name="Index"),
    path("Home", views.index, name="Index"),
    path("Home/Updates", views.index_updates, name="Updates"),
    #Insured things
    path("Insured/New", views.insured_new, name="Insured New"),
    path("Insured/Searching", views.insured_search, name="Insured Searching"),
    #path("insured/searching/{sql bs}", views.insured_new, name="insured new"),
    path("Insured/<int:id>", views.insured_detail, name="Insured Details"),
    #Insurence things
    path("Insurence/New", views.insurence_new, name="Insurence New"),
    path("Insurence/<int:id>", views.insurence_detail, name="Insurence Details"),
    #Questionare things
    path("Questionare/New", views.questionare_new, name="Questionare New"),
    path("Questionare/<int:id>", views.questionare_detail, name="Questionare Details"),
]