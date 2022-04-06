from rest_framework.permissions import BasePermission

# Si es admin podra realziar todas las operaciones CRUD (create, read, update y delete), caso contrario solo para leer (GET)
class IsAdminOrReadOnly(BasePermission):
  # overide del metodo de la clase BasePermission
  def has_permission(self, request, view):
      if request.method == "GET":
        return True
      else:
        return request.user.is_staff

# Si la petición es con el método http GET, entonces si retornamos true podra ver la informacion del api solo con get (solo lectura)
# para el resto de los métodos http (POST, PUT Y DELETE) SOLO USARIOS ADMIN DEL STAFF Podran realizar esa operaciones 
# sino es admin en el "else" se retorna False