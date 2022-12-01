from django.urls import path
from .views import indexPageView, dashboardPageView, infoPageView, dataRender, typePageView, loginPageView, registrationPageView, addFoodPageView, storeFoodItemPageView, registrationPageView2, createUserPageView, loginAuthentication

urlpatterns = [
    path("", indexPageView, name="index"),
    path("visualization", dashboardPageView, name='visualization'),
    path("info", infoPageView, name='info'),
    path("test", dataRender, name='test'),
    path("type", typePageView, name='type'),
    path("login", loginPageView, name = 'login'),
    path("register", registrationPageView, name = 'register'),
    path("addFood", addFoodPageView, name ='addFood'),
    path("store_food", storeFoodItemPageView, name="store_food"),
    path("registration2", registrationPageView2, name="registration2"),
    path("createUser", createUserPageView, name="createUser"),
    path("loginAuthentication", loginAuthentication, name="loginAuthentication")
]