from django.urls import path
from .views import *

urlpatterns = [
    path('',getRoutes,name='getroutes'),
    path('viewdiseases/', viewDisease, name= 'viewdiseases'),
    path('createdisease', createDisease, name='createdisease'),
    path('deletedisease', deleteDisease, name='deletedisease'),
    path('viewsymptom/', viewSymptom, name= 'viewsymptom'),
    path('createsymptom', createSymptom, name='viewsymptom'),
    path('deletesymptom', deleteSymptom, name='deletsymptom'),
]
