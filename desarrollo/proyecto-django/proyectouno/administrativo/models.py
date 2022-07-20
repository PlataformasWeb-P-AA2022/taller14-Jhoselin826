from django.db import models


# Create your models here.

class Propietario(models.Model):
    class Meta:
        verbose_name_plural = "Propietario"

    opciones_tipo = (
        ('ecuatoriana', 'Ecuatoriana'),
        ('peruana', 'Peruana'),
        ('colombiana', 'Colombiana'),

    )
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=150)
    edad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=50, choices=opciones_tipo)

    def __str__(self):
        return "%s - %s - %s - %s" % (
            self.nombre,
            self.apellido,
            self.edad,
            self.tipo
        )

class Departamento(models.Model):
    class Meta:
        verbose_name_plural = "Departamentos"

    costoDepartamento = models.DecimalField(max_digits=10000, decimal_places=2)
    numeroCuartos = models.IntegerField()
    numeroBanios = models.IntegerField()
    valorAlicuota = models.IntegerField()

    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name="departamentos")

    def __str__(self):
        return "%f - %d - %d - %d" % (
            self.costoDepartamento,
            self.numeroCuartos,
            self.numeroBanios,
            self.valorAlicuota
        )