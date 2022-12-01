from django.shortcuts import render
from homepages.models import substance
from homepages.models import daily_log

def indexDashboard(request):
    #Creating substance lists
    substanceName = []
    substanceK = []
    personSubstances = []
    #creating log lists
    personName = []
    MealType = []
    substanceName = []
    nutrientlist = ['K', 'Na', 'Protein', 'Phosphate', 'Water']

    substanceKTotal = 0
    substanceNaTotal = 0
    substanceProteinTotal = 0
    substancePhosTotal = 0
    substanceWaterTotal = 0
#Dynamically change the person_id's value to a variable tomorrow
# This creates list of logs filtered to an individual, loop totals each nutrient for individual
    logs = daily_log.objects.filter(person_id = 2)
    for list in logs:
        personSubstances.append(list.substance.k)
        substanceKTotal += list.substance.k
        substanceNaTotal += list.substance.na
        substanceProteinTotal += list.substance.protein
        substancePhosTotal += list.substance.phosphate
        substanceWaterTotal += list.substance.water

    substancePercentageK = 100*(substanceKTotal/3500)
    substancePercentageNa = 100*(substanceNaTotal/2300)
    substancePercentageProtein = 100*(substanceProteinTotal/(.8*50))
    substancePercentageWater = 100*(substanceWaterTotal/3.7)
    substancePercentagePhos = 100*(substancePhosTotal/3000)

    totalList = [substancePercentageK, substancePercentageNa, substancePercentageProtein, substancePercentagePhos, substancePercentageWater]
    context = {
        'substanceName' : substanceName,
        'substanceK' : substanceK,
        'substanceKTotal' : substanceKTotal,
        'nutrientlist' : nutrientlist,
        'totalList' : totalList,
        'filter' : personName,
        'MealType' : MealType,
        'personSubstances' : personSubstances
    }
    return render(request, 'dashboard/index.html', context)

def visualizationPageView(request):
    #Creating substance lists
    substanceName = []
    substanceK = []
    personSubstances = []
    #creating log lists
    personName = []
    MealType = []
    substanceName = []
    nutrientlist = ['K', 'Na', 'Protein', 'Phosphate', 'Water']

    substanceKTotal = 0
    substanceNaTotal = 0
    substanceProteinTotal = 0
    substancePhosTotal = 0
    substanceWaterTotal = 0
#Dynamically change the person_id's value to a variable tomorrow
# This creates list of logs filtered to an individual, loop totals each nutrient for individual
    logs = daily_log.objects.filter(person_id = 2)
    for list in logs:
        personSubstances.append(list.substance.k)
        substanceKTotal += list.substance.k
        substanceNaTotal += list.substance.na
        substanceProteinTotal += list.substance.protein
        substancePhosTotal += list.substance.phosphate
        substanceWaterTotal += list.substance.water

    substancePercentageK = 100*(substanceKTotal/3500)
    substancePercentageNa = 100*(substanceNaTotal/2300)
    substancePercentageProtein = 100*(substanceProteinTotal/(.8*50))
    substancePercentageWater = 100*(substanceWaterTotal/3.7)
    substancePercentagePhos = 100*(substancePhosTotal/3000)

    totalList = [substancePercentageK, substancePercentageNa, substancePercentageProtein, substancePercentagePhos, substancePercentageWater]
    context = {
        'substanceName' : substanceName,
        'substanceK' : substanceK,
        'substanceKTotal' : substanceKTotal,
        'nutrientlist' : nutrientlist,
        'totalList' : totalList,
        'filter' : personName,
        'MealType' : MealType,
        'personSubstances' : personSubstances
    }
    return render(request, 'dashboard/index2.html', context)