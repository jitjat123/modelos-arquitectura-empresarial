from django.db import models


# Modelo ontologico

class Nivel(models.Model):
    nivel = models.CharField(max_length=30)

    class Meta:
        verbose_name='Nivel'
        verbose_name_plural='Niveles'

    def __str__(self):
        return self.nivel

class Curso(models.Model):
    nombreCurso = models.CharField(max_length=60)
    idioma = models.CharField(max_length=60)
    horas = models.IntegerField()
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    class Meta:
        verbose_name='Curso'
        verbose_name_plural='Cursos'

    def __str__(self):
        return self.nombreCurso

class Estudiante(models.Model):
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=60)
    identificacion =models.IntegerField()
    edad = models.IntegerField()
    genero = models.CharField(max_length=30)
    fechaNacimiento = models.DateTimeField(auto_now=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Estudiante'
        verbose_name_plural='Estudiantes'

    def __str__(self):
        return self.nombre
    

class Pago(models.Model):
    fechaPago = models.DateTimeField(auto_now=False)
    monto = models.FloatField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Pago'
        verbose_name_plural='Pagos'

    def __str__(self):
        return self.estudiante.nombre
    
class Prueba(models.Model):
    idioma = models.CharField(max_length=60)
    calificacion = models.CharField(max_length=20)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    class Meta:
        verbose_name='Prueba'
        verbose_name_plural='Pruebas'

    def __str__(self):
        return self.idioma
    

