from atexit import register
from django.contrib import admin
from .models import User, Injection,Role,Surgery,Dispense_drug
# Register your models here.
admin.site.register(User)
admin.site.register(Injection)
admin.site.register(Surgery)
admin.site.register(Dispense_drug)
admin.site.register(Role)
admin.site.site_header  =  "Administration for the Ideal App"  
admin.site.site_title  =  "Idea App"
admin.site.index_title  =  "Idea app"

