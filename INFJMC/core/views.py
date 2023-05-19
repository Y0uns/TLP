from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Carrera
from .models import Docente




def home(request):
    #return HttpResponse("<h1>home<h1>")
    return render(request, 'core/home.html')

def carreras(request):
    carreras = Carrera.objects.all()
    data = {
            'carreras':carreras
    }
    #return HttpResponse('<h1>carreras<h1>')
    return render(request, 'core/carreras.html', data)


def docentes(request):
    docentes = Docente.objects.all()
    data2= {
            'docentes':docentes
    }
    #return HttpResponse('<h1>docentes<h1>')
    return render(request, 'core/docentes.html', data2)


def nueva_carrera(request):

    if request.POST:
        nombre = request.POST["nombre"]


        #logica y validaciones
        c = Carrera(codigo=1, nombre= nombre, duracion = 1)
        c.save()
        return redirect(carreras)

    return render(request, 'core/nueva_carrera.html')


def nuevo_docente(request):

    if request.POST:
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        email=request.POST["email"]

        c = Docente(nombre=nombre, apellido= apellido , email=email)
        c.save()
        return redirect(docentes)

    return render(request, 'core/nuevo_docente.html')


    