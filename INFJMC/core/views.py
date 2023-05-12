from django.shortcuts import render
from django.http import HttpResponse
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

