from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True, editable=False)


class Mobile(models.Model):
    person = models.ForeignKey(Person, editable=False, on_delete=models.PROTECT)
    mobile = models.CharField(max_length=50)


class Email(models.Model):
    person = models.ForeignKey(Person, editable=False, on_delete=models.PROTECT)
    email = models.EmailField()