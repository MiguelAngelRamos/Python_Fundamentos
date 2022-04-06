from posts.models import Post
from posts.api.serializers import PostSerializer
# trabajar con el ModelViewSet
from rest_framework.viewsets import ModelViewSet

class PostModelViewSet(ModelViewSet):
  serializer_class = PostSerializer # serializador a utilizar
  queryset = Post.objects.all() # la query va utilizar todos los datos que vengan del modelo Post