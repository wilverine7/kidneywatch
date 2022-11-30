from django.db import models

class Person(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.EmailField()
    birthDate = models.DateField()
    gender = models.CharField(max_length=1)
    weight = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return (self.id)
class ComorbidityType(models.Model):
    comorbidityTypeDescription = models.CharField(max_length=100)

    def __str__(self):
        return (self.id)

class DailyLog(models.Model):
    date = models.DateField()

    def __str__(self):
        return (self.id)

class Meal(models.Model):

    def __str__(self):
        return (self.id)

class MealType(models.Model):
    mealTypeDescription = models.CharField(max_length=100)

    def __str__(self):
        return (self.id)

class Substance(models.Model):
    name = models.CharField(max_length=30)
    K = models.FloatField()
    Na = models.FloatField()
    protein = models.FloatField()
    Phos = models.FloatField()
    water = models.FloatField()