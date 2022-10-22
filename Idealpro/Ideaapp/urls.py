from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import Ceo, addToCsuiteGroup, Home
urlpatterns = [
    path("", Home, name="home" ),
    path("only-for-ceo", Ceo, name="only-for-ceo" ),
    path("add-to-ceo-group", addToCsuiteGroup, name="addtoceogroup" )
]