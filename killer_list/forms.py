from .models import Person
from django import forms


class PersonForm(forms.ModelForm):
    name = forms.CharField(max_length=20, label="First Name")
    surname = forms.CharField(max_length=20, label="Surname")
    mobile = forms.CharField(label="mobile number", min_length=9, max_length=9, widget=forms.NumberInput, required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = Person
        fields = [
            'name',
            'surname',
            'mobile',
            'email',
        ]