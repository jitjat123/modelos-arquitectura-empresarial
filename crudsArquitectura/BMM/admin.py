from django.contrib import admin
from .models import *
# Register your models here.

class misionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Mision, misionAdmin)

class visionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vision, visionAdmin)

class estrategiaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Estrategia, estrategiaAdmin)

class objetivoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Objetivo, objetivoAdmin)

class tacticaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tactica, tacticaAdmin)

class metaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Meta, metaAdmin)