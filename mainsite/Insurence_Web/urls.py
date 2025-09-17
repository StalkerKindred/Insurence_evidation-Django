from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("insured/<int:id>/", views.insured_detail, name="Insured Details"),
    path("insurence/<int:id>/", views.insurence_detail, name="Insurence Details"),
    path("questionare/<int:id>/", views.questionare_detail, name="Questionare Details"),
]