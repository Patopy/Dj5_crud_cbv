from django.db import models

# Create your models here.
class Cliente(models.Model):
    OP_SEXO = [
        ("F", "Femenino"),
        ("M", "Masculino"),
        ("I", "Indefinido")
    ]
        
    nombre = models.CharField(max_length=30)
    edad   = models.IntegerField(blank=True, null=True)
    sexo   = models.CharField(max_length=1, choices=OP_SEXO, default='I')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tb_cliente'
        ordering = ["nombre"]
    