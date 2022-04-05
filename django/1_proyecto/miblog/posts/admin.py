from django.contrib import admin
from posts.models import Post

# Register your models here.
@admin.register(Post) # Registrando en el panel de admistrador el modelo Post
class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'created_at']
