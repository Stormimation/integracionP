from django.contrib import admin
from .models import Medico, UsuarioP4, Hora, Dia, Mes, Agendar, UsuarioM, UsuarioS, Agendar6,Region,Comuna,Provincia,sexo, AgendarA

# Register your models here.



class MedicoAdmin(admin.ModelAdmin):                                              #Quitar Simbolo de comentario solo para fines administrativos
    list_display=("idMedico","nombreMedico", "apellidoMedico","especialidad")

class UsuarioPAdmin(admin.ModelAdmin):
    list_display=("rut","email","nombre","apellidos","region","provincia","comuna","edad","sexo","password")   

class UsuarioMAdmin(admin.ModelAdmin):
    list_display=("id","nombre","password")

class UsuarioSAdmin(admin.ModelAdmin):
    list_display=("id","nombre","password")  

class Agendar5Admin(admin.ModelAdmin):
    list_display=("idHora", "dia", "mes", "hora", "nombre", "medico") 

class AgendarAAdmin(admin.ModelAdmin):
    list_display=("idHora","dia","mes","hora","nombre","medico","mensaje")       
           

class DiaAdmin(admin.ModelAdmin):            #Quitar Simbolo de comentario solo para fines administrativos
    list_display=["dia"]

class HoraAdmin(admin.ModelAdmin):
    list_display=["hora"]

class MesAdmin(admin.ModelAdmin):
    list_display=["mes"]

class RegionAdmin(admin.ModelAdmin):
    list_display=["region"]

class ProvinciaAdmin(admin.ModelAdmin):
    list_display=["provincia"]

class ComunaAdmin(admin.ModelAdmin):
    list_display=["comuna"]

class sexoAdmin(admin.ModelAdmin):
    list_display=["sexo"]        

    

admin.site.register(Region,RegionAdmin)
admin.site.register(Provincia,ProvinciaAdmin)
admin.site.register(Comuna,ComunaAdmin)
admin.site.register(sexo,sexoAdmin)
admin.site.register(UsuarioP4,UsuarioPAdmin)
admin.site.register(UsuarioM, UsuarioMAdmin)
admin.site.register(UsuarioS, UsuarioSAdmin)
admin.site.register(Hora,HoraAdmin)              #Quitar Simbolo de comentario solo para fines administrativos
admin.site.register(Dia,DiaAdmin)
admin.site.register(Mes,MesAdmin)
admin.site.register(Agendar)
admin.site.register(Agendar6, Agendar5Admin)
admin.site.register(AgendarA, AgendarAAdmin)
admin.site.register(Medico, MedicoAdmin)