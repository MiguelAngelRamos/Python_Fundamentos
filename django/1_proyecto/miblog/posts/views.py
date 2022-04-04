from django.http import HttpResponse
from django.views.generic.base import View

# Crear nuestras vistas
class HelloWorld(View):
  def get(self, request):
    return HttpResponse(content='Hola Mundo, mi nombre es Miguel')
  
  