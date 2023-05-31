from django.contrib import admin
from .models import *
# Register your models here.


class estudianteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Estudiante, estudianteAdmin)

class pagoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pago, pagoAdmin)

class pruebaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Prueba, pruebaAdmin)

class nivelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Nivel, nivelAdmin)

class cursoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Curso, cursoAdmin)

