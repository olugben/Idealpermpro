from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import HttpResponse 
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Surgery, Injection,  Dispense_drug, Role, User
from django.contrib.auth.models import Group


# Create your views here.
def Error(request):
    return Http404("Please login first")

@login_required(login_url='/admin')
def addToCsuiteGroup(request):
        group=Group.objects.get(name="C-level")
        request.user.groups.add(group)
        return render(request, "addtocsuite.html",{"user":request.user,"group":group })
     

def group_required(*group_names):
    def in_groups(user):
        print(user)
        return user.is_active and (user.is_superuser or bool(user.groups.filter(name__in=group_names)))
    return user_passes_test(in_groups)
@login_required(login_url="/admin")
@group_required('C-level')
def Ceo(request):
        
        if request.user.groups.filter(name="C-level"):
            use=User.objects.all()
            role=Role.objects.all()
            print(use)
            return render(request,"ceo.html",{"user":use,"role":role})
        else:
            return HttpResponseNotFound("<h1>You dont have sufficient permission</h1>") 
def Home(request):
    return render(request, "home.html")               