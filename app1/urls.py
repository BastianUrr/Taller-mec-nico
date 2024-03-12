from django.urls import path
from .views import vista, principal, contacto, registro, limpiezaMotor
from .views import cambioPastillas, aliniamiento, cambioAceite

from .views import base, poblarBaseDatos, guardado, guardado2, formTrabajo, extension, index
from .views import experimento1, guardado3, trabajo, cate, mecanico, guardado3

urlpatterns = [
    path('', index, name=''),
    path('principal',principal, name='principal'),
    path('contacto',contacto, name='contacto'),
    path('vista', vista, name='vista'),
    path('registro',registro, name='registro'),
    path('limpiezaMotor',limpiezaMotor, name='limpiezaMotor'),
    path('cambioPastillas',cambioPastillas, name='cambioPastillas'),
    path('aliniamiento',aliniamiento, name='aliniamiento'),
    path('cambioAceite',cambioAceite, name='cambioAceite'),




    path('poblarBaseDatos', poblarBaseDatos, name='poblarBaseDatos'),
    path('guardado', guardado, name='guardado'),
    path('formTrabajo', formTrabajo, name='formTrabajo'),
    path('base', base, name='base'),
    path('extension', extension, name='extension'),
    path('guardado2', guardado2, name='guardado2'),
    path('categoria/<cate>', cate, name='cate'),
    path('trabajo/<pk>', trabajo, name='trabajo'),
    path('mecanico/<pk>', mecanico, name='meca'),
    path('guardado3', guardado3, name='guardado3'),





    path('exp1', experimento1, name='exp1'),
    path('guardado3', guardado3, name='guardado3')
    
    
]
