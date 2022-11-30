from django.shortcuts import render
from homepages.models import substance

def indexDashboard(request):
    substanceName = []
    substanceK = []
    nutrientlist = ['K', 'Na', 'Protein', 'Phosphate', 'Water']
    substanceKTotal = 0
    substanceNaTotal = 0
    substanceProteinTotal = 0
    substancePhosTotal = 0
    substanceWaterTotal = 0
    for list in substance.objects.all():
        substanceName.append(list.name)
        substanceK.append(list.k)
        substanceKTotal += list.k
        substanceNaTotal += list.na
        substanceProteinTotal += list.protein
        substancePhosTotal += list.phosphate
        substanceWaterTotal += list.water
    substancePercentageK = 100*(substanceKTotal/3500)
    substancePercentageNa = 100*(substanceNaTotal/2300)
    substancePercentageProtein = 100*(substanceProteinTotal/(.8*50))
    substancePercentageWater = 100*(substanceWaterTotal/3.7)
    substancePercentagePhos = 100*(substancePhosTotal/3000)
    # substanceProteinTotal = substanceProteinTotal * 1000
    # substanceWaterTotal = 1000000
    # for list in substanceK:
    #     substanceKTotal = int(substanceK[list]) + int(substanceKTotal)
    totalList = [substancePercentageK, substancePercentageNa, substancePercentageProtein, substancePercentagePhos, substancePercentageWater]
    context = {
        'substanceName' : substanceName,
        'substanceK' : substanceK,
        'substanceKTotal' : substanceKTotal,
        'nutrientlist' : nutrientlist,
        'totalList' : totalList
    }
    return render(request, 'dashboard/index.html', context)

def visualizationPageView(request):
    return render(request, 'partials/main.html')
