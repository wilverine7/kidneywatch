from django.urls import path
from .views import indexDashboard, visualizationPageView
urlpatterns = [
    path('', indexDashboard, name="dashboard"),
    path('index2', visualizationPageView, name="index2")
]
