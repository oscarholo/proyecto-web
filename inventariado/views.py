from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Ubicaciones, Dispositivos, Traslados
from .forms import UbicacionForm, DispositivoForm, TrasladoForm

def index(request):
    """Página principal del sistema"""
    return render(request, 'inventariado/index.html')

def lista_dispositivos(request):
    """Lista todos los dispositivos"""
    dispositivos = Dispositivos.objects.all().select_related('id_ubi')
    return render(request, 'inventariado/lista_dispositivos.html', {
        'dispositivos': dispositivos
    })

def agregar_dispositivo(request):
    """Formulario para agregar dispositivo"""
    if request.method == 'POST':
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_dispositivos')
    else:
        form = DispositivoForm()
    
    return render(request, 'inventariado/formulario.html', {
        'form': form,
        'titulo': 'Agregar Dispositivo',
        'url_volver': 'lista_dispositivos'
    })

def agregar_ubicacion(request):
    """Formulario para agregar ubicación"""
    if request.method == 'POST':
        form = UbicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UbicacionForm()
    
    return render(request, 'inventariado/formulario.html', {
        'form': form,
        'titulo': 'Agregar Ubicación',
        'url_volver': 'index'
    })

def agregar_traslado(request):
    """Formulario para registrar traslado"""
    if request.method == 'POST':
        form = TrasladoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_dispositivos')
    else:
        form = TrasladoForm()
    
    return render(request, 'inventariado/formulario.html', {
        'form': form,
        'titulo': 'Registrar Traslado',
        'url_volver': 'lista_dispositivos'
    })
def eliminar_dispositivo(request, id_dis):
    """Eliminar un dispositivo"""
    dispositivo = get_object_or_404(Dispositivos, pk=id_dis)
    
    if request.method == 'POST':
        dispositivo.delete()
        return redirect('lista_dispositivos')
    
    return render(request, 'inventariado/confirmar_eliminar.html', {
        'objeto': dispositivo,
        'tipo_objeto': 'dispositivo',
        'url_volver': 'lista_dispositivos'
    })

def eliminar_ubicacion(request, id_ubi):
    """Eliminar una ubicación"""
    ubicacion = get_object_or_404(Ubicaciones, pk=id_ubi)
    
    if request.method == 'POST':
        ubicacion.delete()
        return redirect('index')
    
    return render(request, 'inventariado/confirmar_eliminar.html', {
        'objeto': ubicacion,
        'tipo_objeto': 'ubicación',
        'url_volver': 'index'
    })

def eliminar_traslado(request, id_tras):
    """Eliminar un traslado"""
    traslado = get_object_or_404(Traslados, pk=id_tras)
    
    if request.method == 'POST':
        traslado.delete()
        return redirect('index')
    
    return render(request, 'inventariado/confirmar_eliminar.html', {
        'objeto': traslado,
        'tipo_objeto': 'traslado',
        'url_volver': 'index'
    })