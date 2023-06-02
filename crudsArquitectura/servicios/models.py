from django.db import models
from ontologico.models import Curso
# Create your models here.

class BullUnillanos(models.Model):
    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name='Bull Unillanos'

    def __str__(self):
        return self.nombre
    
class Actor(models.Model):
    nombre = models.CharField(max_length=60)
    cedula = models.CharField(max_length=12)
    bull = models.ForeignKey(BullUnillanos, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Actor'
        verbose_name_plural='Actores'

    def __str__(self):
        return self.nombre
    
class LineaNegocio(models.Model):
    nombre = models.CharField(max_length=60)
    bull = models.ForeignKey(BullUnillanos, on_delete=models.CASCADE)

    class Meta:
        verbose_name= 'Linea de negocio'

    def __str__(self):
        return self.nombre
    
class EmisionCertificado(models.Model):
    certificado = models.CharField(max_length=150)
    fecha = models.DateField(auto_now=True)

    class Meta:
        verbose_name='Emision de certificado'

    def __str__(self):
        return self.certificado
    

class ObjetoNegocio(models.Model):
    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    certificado = models.ForeignKey(EmisionCertificado, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Objeto de negocio'

    def __str__(self):
        return self.nombre
    

class ServicioNegocio(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=300)
    objeto = models.ForeignKey(ObjetoNegocio, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    bull = models.ForeignKey(BullUnillanos, on_delete=models.CASCADE)
    linea = models.ForeignKey(LineaNegocio, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Servicio de negocio'

    def __str__(self):
        return self.nombre