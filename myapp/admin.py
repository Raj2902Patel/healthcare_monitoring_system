from django.contrib import admin
from .models import appointmenttable,commenttable,contacttable,registertable

# Register your models here.

class showappointmenttable(admin.ModelAdmin):
    list_display = ['Name','Email','Date','Departement','Number','Message']

admin.site.register(appointmenttable,showappointmenttable)

class showcommenttable(admin.ModelAdmin):
    list_display = ['Name','Email','Website','Message']

admin.site.register(commenttable,showcommenttable)

class showcontacttable(admin.ModelAdmin):
    list_display = ['Name','Email','Subject','Message']

admin.site.register(contacttable,showcontacttable)

class showregistertable(admin.ModelAdmin):
    list_display = ['Name','Email','Number','Password','Address']

admin.site.register(registertable,showregistertable)