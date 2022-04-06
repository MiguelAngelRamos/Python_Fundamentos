#from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

# Crear nuestras vistas
class HelloWorld(View):
  def get(self, request):
    # suponiendo que hacemos una petición a la base de datos
    data = {
      'name': 'Miguel',
      'last_name': 'Ramos',
      'codes': ['Java', 'JavaScript', 'Python']
    }
    return render(request, 'hello_world.html', context = data)
    #return HttpResponse(content='Hola Mundo, mi nombre es Miguel')
  