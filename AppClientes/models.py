from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    edad   = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre