from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import HttpResponse 
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Surgery, Injection,  Dispense_drug, Role, User
from django.contrib.auth.models import Group


# Create your views here.

@login_required
def addToPremiumGroup(request):
    group=Group.objects.get(name="premium")
    request.user.groups.add(group)
    return render(request, "addtopremium.html",{"user":request.user,"group":group })

def group_required(*group_names):
    def in_groups(user):
        print(user)
        return user.is_active and (user.is_superuser or bool(user.groups.filter(name__in=group_names)))
    return user_passes_test(in_groups)
@group_required('premium')
def Ceo(request):
        print(request.user)
        if request.user.groups.filter(name="C-level"):
            user=User.objects.all()
            role=Role.objects.all()
            return render(request,"ceo.html",{"user":user})
        else:
            return HttpResponse("you are not allowed")    