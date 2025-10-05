from django.urls import path

from . import views

urlpatterns = [
    # - home
    path("", views.index, name="index"),
    path("home", views.index, name="index"),
    path("home/updates", views.index_updates, name="updates"),
    path("insured/new/", views.insured_new, name="insured new"),
    path("insured/<int:id>/", views.insured_detail, name="Insured Details"),
    path("insurence/<int:id>/", views.insurence_detail, name="Insurence Details"),
    path("questionare/<int:id>/", views.questionare_detail, name="Questionare Details"),
]