from django.contrib import admin
from intranet import models

@admin.register(models.CadPaciente)
class CadPaciente(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone','cpf',)

@admin.register(models.Medico) 
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'crm', 'especialidade',)