from .models import Person, Mobile, Email
from django import forms


class PersonForm(forms.ModelForm):
    name = forms.CharField(max_length=20, label="First Name")
    surname = forms.CharField(max_length=20, label="Surname")

    class Meta:
        model = Person
        fields = [
            'name',
            'surname',
        ]


class MobileForm(forms.ModelForm):
    mobile = forms.CharField(label="mobile number", min_length=9, max_length=9, widget=forms.NumberInput, required=False)

    class Meta:
        model = Mobile
        fields = [
            'mobile',
        ]


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        mode = Email
        fields = [
            'email',
        ]