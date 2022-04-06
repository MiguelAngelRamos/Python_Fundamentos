from rest_framework.serializers import ModelSerializer
from posts.models import Post

class PostSerializer(ModelSerializer):
  class Meta:
    model = Post
    fields = ['title', 'description', 'order', 'created_at']
    
# el serializador utiliza el modelo post y le indicamos
# los campos que va a retornar