from django.contrib import admin
from .models import comorbidity_type, person, daily_log, meal_type, substance, meal

admin.site.register(comorbidity_type)
admin.site.register(person)
admin.site.register(daily_log)
admin.site.register(meal_type)
admin.site.register(substance)
admin.site.register(meal)

# Register your models here.
