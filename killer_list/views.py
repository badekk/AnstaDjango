from django.shortcuts import render
from .forms import PersonForm, EmailForm, MobileForm
from .models import Person, Mobile, Email
# Create your views here.


def people_add(request):
    form = PersonForm(request.POST or None)
    email_form = EmailForm(request.POST or None)
    mobile_form = MobileForm(request.POST or None)
    if form.is_valid() and email_form.is_valid() and mobile_form.is_valid():
        form.save()
        email_form.save()
        mobile_form.save()
        form = PersonForm()
        mobile_form = MobileForm()
        email_form = EmailForm()
    context = {
        "form": form,
        'mobile': mobile_form,
        'email': email_form,
        }

    return render(request, "killer_list/add_people.html", context)


def people_list_view(request):
    queryset = Person.objects.all()
    context = {
        "object_list": queryset,
    }
    return render(request, "killer_list/list_of_people.html", context)
