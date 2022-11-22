from django.http import *
from django.shortcuts import render
from .forms import UserForm
from .models import Person


def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})


def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")


def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})

    except Person.DoesNotExist:
        return HttpResponseNotFound("Клиент не найден")


def delete(request, id):

    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("Клиент не найден")

def about(request):
    return HttpResponse("About")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")


def home(request):
    return render(request,"firstapp/home.html")