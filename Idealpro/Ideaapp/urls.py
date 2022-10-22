from django.contrib import admin
from django.urls import path
from .views import Ceo, addToCsuiteGroup
urlpatterns = [
     path("ceo", Ceo ),
    path("addtocsuite", addToCsuiteGroup )
]