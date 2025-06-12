from django.db import models

class MateriaPrima(models.Model):
    tipo_da_materia = models.CharField(max_length=120)

    def __str__(self):
        return self.tipo_da_materia