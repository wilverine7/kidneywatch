from django.urls import path
from .views import indexDashboard 
urlpatterns = [
    path('', indexDashboard, name="dashboard"),
]
