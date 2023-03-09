from django.shortcuts import render
from django.contrib.staticfiles import finders
from django.core.paginator import Paginator
from .models import Language, Country
import json
import os

def get_countries():
    with open(finders.find("country-by-languages.json"), "r", encoding="utf-8") as file:
        countries = json.load(file)
        return countries


# Create your views here.
def index(request):
    return render(request, "index.html")

def countries_list(request, letter = False):
    if letter:
        countries = Country.objects.filter(country__startswith = letter.upper())
    else:
        countries = Country.objects.all()
    paginator = Paginator(countries, 10)
    countries = paginator.get_page(request.GET.get("page", 1))
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return render(request, "countries-list.html", {"countries" : countries, "letters" : letters, "paginator" : paginator})

def languages_list(request):
    languages = Language.objects.all()
    return render(request, "languages-list.html", {"languages" : languages})

def country(request, id):
    country = Country.objects.filter(id=id).first()
    languages = country.languages.all()
    return render(request, "country.html", {"country" : country, "languages" : languages})

def language(request, id):
    language = Language.objects.filter(id = id).first()
    countries = Country.objects.filter(languages__in = [language])
    return render(request, "language.html", {"language" : language, "countries" : countries})

def import_countries(request):
    countries = get_countries()
    languages = []
    for country in countries:
        for language in country.get("languages"):
            if language not in languages:
                languages.append(language)

    for language in languages:
        Language(language = language).save()
    
    for country in countries:
        print(country.get("languages"))
        country_obj = Country(
            country = country.get("country")
        )
        country_obj.save()
        
        for language in country.get("languages"):
            country_obj.languages.add(Language.objects.get(language = language))
        
        country_obj.save()        
    return render(request, "index.html")