from django.db import models
from datetime import datetime, timedelta

class comorbidity_type(models.Model):
    comorbidity_type_description = models.CharField(max_length=100)

    def __str__(self):
        return (self.comorbidity_type_description)

class person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    birth_date = models.DateField(default=datetime.today)
    gender = models.CharField(max_length=1)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    personname = models.CharField(max_length=30)
    password = models.CharField(max_length=150)
    comorbidity_type = models.ForeignKey(comorbidity_type, on_delete=models.DO_NOTHING)

    def __str__(self):
        return (self.full_name)
    
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

class meal_type(models.Model):
    meal_type_description = models.CharField(max_length=100)

    def __str__(self):
        return (self.meal_type_description)

class substance(models.Model):
    name = models.CharField(max_length=100)
    k = models.FloatField()
    na = models.FloatField()
    protein = models.FloatField()
    phosphate = models.FloatField()
    water = models.FloatField()

    def __str__(self):
        return(self.name)
    

class daily_log(models.Model):
    date = models.DateField(default=datetime.today)
    person = models.ForeignKey(person, on_delete=models.CASCADE)
    meal_type = models.ForeignKey(meal_type, on_delete=models.DO_NOTHING)
    substance = models.OneToOneField(substance, on_delete=models.DO_NOTHING)

    def __str__(self):
        return (str(self.date))

