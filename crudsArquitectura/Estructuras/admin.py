from django.contrib import admin
from .models import *
# Register your models here.

class direccionAdmin(admin.ModelAdmin):
    pass

admin.site.register(DireccionEjecutiva, direccionAdmin)

class departamentoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Departamento, departamentoAdmin)

class trabajadorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Trabajador, trabajadorAdmin)

class actividadAdmin(admin.ModelAdmin):
    pass

admin.site.register(Actividad, actividadAdmin)

class recursoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Recurso, recursoAdmin)