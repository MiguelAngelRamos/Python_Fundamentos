from rest_framework.views import APIView # esta importacion es la que nos va permitir codificar el POST, DELETE, UPDATE ETC.....
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post
from posts.api.serializers import PostSerializer

# trabajar con el ViewSet
from rest_framework.viewsets import ViewSet

class PostViewSet(ViewSet):
  # traer todos los posts equivalente al get ViewSet se trabaja como "list"
  def list(self, request):
    serializer = PostSerializer(Post.objects.all(), many=True)
    return Response(status = status.HTTP_200_OK, data=serializer.data)
  
  # para crear posts con ViewSet se trabaja como "create"
  def create(self, request):
    serializer = PostSerializer(data=request.POST)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(status=status.HTTP_200_OK, data=serializer.data)
  
  # para obtener el parametro id
  def retrieve(self, request, pk: int):
    post = PostSerializer(Post.objects.get(pk=pk))
    return Response(status=status.HTTP_200_OK, data=post.data)







# class PostApiView(APIView):
#   def get(self, request):
#     # posts = Post.objects.all()
#     #posts = [ post.title for post in Post.objects.all()]
#     #return Response(status = status.HTTP_200_OK, data = posts)
#     serializer = PostSerializer(Post.objects.all(), many=True) # devuelva el array completo de posts
#     return Response(status = status.HTTP_200_OK, data = serializer.data)
  
#   def post(self, request):
#     serializer = PostSerializer(data=request.POST) # enviamos al serializador la información ingresada por el usuario
#     serializer.is_valid(raise_exception=True) # si algun dato no es válido nos va devolver una excepcion
#     serializer.save() # para guardar la información en la base de datos
#     return Response(status=status.HTTP_200_OK, data = serializer.data)