from django.db import models

# Create your models here.
from django.db import models
from django import db 
from django.db import models 
from django.contrib.auth.models import PermissionsMixin,User, AbstractUser
from django.contrib.auth.models import AbstractBaseUser, UserManager, BaseUserManager
from django.conf import settings 
 
from django.conf import settings 
from django.contrib.sessions.models import Session   
# Create your models here.

class Injection(models.Model):
    injection_name=models.CharField(max_length=24)
    injection_uses=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.injection_name   
class Dispense_drug(models.Model):
    drug_name=models.CharField(max_length=24)
    drug_uses=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.drug_name 
class Surgery(models.Model):
    procedure_name=models.CharField(max_length=24)
    fatality=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.procedure_name
class Role(models.Model):
    DOCTOR=1
    SURGEON=2
    NURSES=3
    PHARMACY=4
    ADMIN=5
    ROLE_CHOICES=(
        (DOCTOR,"doctor"),
        (SURGEON,"surgeon"),
        (NURSES,"nurses"),
        (PHARMACY,"pharmacy"),
        (ADMIN,"admin")
    )
    id=models.PositiveSmallIntegerField(choices=ROLE_CHOICES,primary_key=True)
    user=models.ManyToManyField(User)
# class User(User, PermissionsMixin):
#    role=models.ManyToManyField(Role, related_name="okay" )
