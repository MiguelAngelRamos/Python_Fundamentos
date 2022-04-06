from posts.models import Post
from posts.api.serializers import PostSerializer
# trabajar con el ModelViewSet
from rest_framework.viewsets import ModelViewSet
# PERMISOS REST FRAMEWORK
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
# PERMISO PERSONALIZADO
from posts.api.permissions import IsAdminOrReadOnly

class PostModelViewSet(ModelViewSet):
  # permission_classes = [IsAuthenticated] # usuarios autentificados vamos a pedirles un token autenticacion "JWT TOKEN"
  # permission_classes = [IsAdminUser] # solo usarios administradores que tiene "staff status"
  # permission_classes = [IsAuthenticatedOrReadOnly] 
  permission_classes = [IsAdminOrReadOnly] 
  serializer_class = PostSerializer # serializador a utilizar
  queryset = Post.objects.all() # la query va utilizar todos los datos que vengan del modelo Post