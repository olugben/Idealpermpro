from django.contrib import admin
from django.urls import path
from .views import Ceo, addToPremiumGroup
urlpatterns = [
     path("ceo", Ceo ),
    path("addtopremium", addToPremiumGroup )
]