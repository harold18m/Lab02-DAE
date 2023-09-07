from django.urls import path

from .import views

app_name='encuesta'

urlpatterns = [
    path('',views.index,name="index"),
    path('formulario',views.ejercicio1,name="ejercicio1"),
    path('formulario/resultado',views.calcular,name="resultado"),
    path('formulario2',views.ejercicio2,name="ejercicio2"),
    path('formulario2/resultado2',views.calcularEdad,name="resultado2"),
    path('formulario3',views.ejercicio3,name="ejercicio3"),
    path('formulario3/resultado3',views.calcularVolumen,name="resultado3"),
]