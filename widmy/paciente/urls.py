from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('pacientes/', views.pacientes_list),
    path('pacientecreate/', csrf_exempt(views.paciente_create), name='pacienteCreate'),]
    #path('', views.pacientes_view, name='pacientes_view'),
    
    #path('<int:pk>', views.paciente_view, name='paciente_view'),
    #path('altaprioridad',views.alta_prioridad, name='alta_prioridad')]