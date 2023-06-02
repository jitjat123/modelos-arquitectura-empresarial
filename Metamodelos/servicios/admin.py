from django.contrib import admin
from .models import * 
# Register your models here.

class bullAdmin(admin.ModelAdmin):
    pass

admin.site.register(BullUnillanos, bullAdmin)

class actorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Actor, actorAdmin)

class lineaAdmin(admin.ModelAdmin):
    pass

admin.site.register(LineaNegocio, lineaAdmin)

class servicioAdmin(admin.ModelAdmin):
    pass

admin.site.register(ServicioNegocio, servicioAdmin)

class objetoAdmin(admin.ModelAdmin):
    pass

admin.site.register(ObjetoNegocio, objetoAdmin)


class certificadoAdmin(admin.ModelAdmin):
    pass

admin.site.register(EmisionCertificado, certificadoAdmin)




