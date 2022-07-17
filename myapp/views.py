from django.shortcuts import render
from myapp.forms import FamiliarFormulario, FamiliarBusqueda
from myapp.models import Familiares

# Create your views here.

def inicio(request):
    return render(request, "myapp/index.html", {})

def datos_familiares(request):
    context = {"familiares": Familiares.objects.all()}
    return render(request, "myapp/familiares.html", context)

def formulario_familiar(request):
    if request.method == "POST":
        
        mi_formulario = FamiliarFormulario(request.POST)
        if  mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data 
            familiar = Familiares(nombre=datos["nombre"], apellido=datos["apellido"], dni=datos["dni"])
            familiar.save()
            return render(request, "myapp/verificacion.html", {"mensaje":"Familiar agregado con exito!"})
   
    else:
        mi_formulario = FamiliarFormulario()
    
    return render(request, "myapp/formulario.html", {"mi_formulario":mi_formulario})


def formulario_busqueda(request):

    busqueda_formulario = FamiliarBusqueda()


    if request.GET:
        busqueda_formulario = FamiliarBusqueda(request.GET)
        if  busqueda_formulario.is_valid():      
            familiares = Familiares.objects.filter(nombre=busqueda_formulario.cleaned_data.get("criterio")).all()
            return render(request, "myapp/busqueda.html", {"busqueda_formulario": busqueda_formulario, "familiares": familiares})
        else:
            familiares = []
            
    return render(request, "myapp/busqueda.html", {"busqueda_formulario": busqueda_formulario})