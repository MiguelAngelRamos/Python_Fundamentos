from django.db import models
# Por medio de este modelo se va crear una tabla con el orm django
class Post(models.Model):
  title = models.CharField(max_length=255) # cuando queremos limitar el texto
  description = models.TextField() # cuando no queremos limitar el texto
  order = models.IntegerField() # orden en que se van creando
  created_at = models.DateTimeField(auto_now_add=True) # va crear la fecha actual automaticamente
