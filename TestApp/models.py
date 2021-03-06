from django.db import models
from django.db.models import Avg
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey, ManyToManyField


# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    icon_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.company_name


class Location(models.Model):
    location_name = models.CharField(max_length=255)
    company = models.ManyToManyField(Company)

    def __str__(self):
        return self.location_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)
    company = ManyToManyField(Company)

    def __str__(self):
        return self.tag_name


class Level(models.Model):
    level_name = models.CharField(max_length=255)
    company = ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.level_name

    @property
    def avg_salary(self):
        return self.employee_set.aggregate(Avg('totalyearlycompensation'))


class Gender(models.Model):
    gender = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        if not self.gender:
            return 'null'
        return self.gender


class Race(models.Model):
    race = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        if not self.race:
            return 'null'
        return self.race


class Acad_level(models.Model):
    acad_level = CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        if not self.acad_level:
            return 'null'
        return self.acad_level


class Employee(models.Model):
    timestamp = models.DateTimeField()
    yearsofexperience = models.IntegerField()
    yearsatcompany = models.IntegerField()
    totalyearlycompensation = models.IntegerField()
    base_salary = models.IntegerField()
    stockgrantvalue = models.IntegerField()
    bonus = models.IntegerField()
    remote = models.BooleanField(default=False)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True)
    academic_level = models.ForeignKey(Acad_level, on_delete=models.SET_NULL, null=True)

    @property
    def company(self):
        c = self.level.company
        return {"company": c.company_name, "icon_url": c.icon_url}
