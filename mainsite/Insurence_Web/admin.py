from django.contrib import admin

# Register your models here.

from .models import InsurerEmployees, InsuredPersons, InsurenceQuestionare, Insurence

admin.site.register(InsurerEmployees)
admin.site.register(InsuredPersons)
admin.site.register(InsurenceQuestionare)
admin.site.register(Insurence)