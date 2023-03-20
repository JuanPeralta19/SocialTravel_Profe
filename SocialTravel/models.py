from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    carousel_caption_title = models.CharField(max_length=30)
    carousel_caption_description = models.CharField(max_length=80)
    heading = models.CharField(max_length=15)
    description = models.CharField(max_length=120)
    publicador = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "publicador")
    imagen = models.ImageField(upload_to = "posts", null = True, blank = True)

    @property
    def imagen_url(self):
        return self.imagen.url if self.imagen else ''

    def __str__(self):
        return f"{self.id} - {self.heading}"