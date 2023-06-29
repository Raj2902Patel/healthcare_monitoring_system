from django.contrib import admin
from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.patient,name='patient'),
    path('doctor',views.index,name='index'),
    path('temperaturetable',views.datatables,name='temperaturetable'),
    path('oxygentable',views.oxygen,name='oxygentable'),
    path('pulsetable',views.pulse,name='pulsetable'),
    path('ecgtable',views.ecg,name='ecgtable'),
    path('appointmenttable',views.raj,name='appointmenttable'),
    path('patient',views.patient,name='patient'),
    path('pecg',views.pecg,name='pecg'),
    path('poxygen',views.poxygen,name='poxygen'),
    path('ppulse',views.ppulse,name='ppulse'),
    path('ptemp',views.ptemp,name='ptemp'),
]
