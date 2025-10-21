from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dispositivos/', views.lista_dispositivos, name='lista_dispositivos'),
    path('dispositivos/agregar/', views.agregar_dispositivo, name='agregar_dispositivo'),
    path('dispositivos/eliminar/<int:id_dis>/', views.eliminar_dispositivo, name='eliminar_dispositivo'),
    path('ubicaciones/agregar/', views.agregar_ubicacion, name='agregar_ubicacion'),
    path('ubicaciones/eliminar/<int:id_ubi>/', views.eliminar_ubicacion, name='eliminar_ubicacion'),
    path('traslados/agregar/', views.agregar_traslado, name='agregar_traslado'),
    path('traslados/eliminar/<int:id_tras>/', views.eliminar_traslado, name='eliminar_traslado'),
]