from django.shortcuts import render

def indexDashboard(request):
    context = {
        
    }
    return render(request, 'dashboard/index.html', context)

def visualizationPageView(request):
    return render(request, 'partials/main.html')
