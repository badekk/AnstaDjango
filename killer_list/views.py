from django.shortcuts import render
from .forms import PersonForm
from .models import Person, Mobile, Email
# Create your views here.


def people_add(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PersonForm()

    context = {
        "form": form
        }

    return render(request, "killer_list/add_people.html", context)


def people_list_view(request):
    queryset = Person.objects.all()
    mobiles = Mobile.objects.all()
    emails = Email.objects.all()
    context = {
        "object_list": queryset,
        "mobile_numbers": mobiles,
        "email_adresses": emails,
    }
    return render(request, "killer_list/list_of_people.html", context)
