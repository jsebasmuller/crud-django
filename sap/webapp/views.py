from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from personas.forms import PersonaForm
from personas.models import Persona


# Create your views here.

def bienvenido(request):
    no_personas = Persona.objects.count()
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenido.html', {'no_personas': no_personas, 'personas': personas})

def detallePersona(request, id):
    persona = get_object_or_404(Persona, pk = id)
    return render(request, 'persona/detalle-persona.html', {'persona': persona})

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()
    return render(request, 'persona/nuevo.html', {'formaPersona': formaPersona})

def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm(instance = persona)
    return render(request, 'persona/editar.html', {'formaPersona': formaPersona})

def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')