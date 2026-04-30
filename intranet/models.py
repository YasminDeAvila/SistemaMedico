from django.db import models

class CadPaciente(models.Model):
    nome = models.CharField(max_length=30)
    cpf =  models.CharField(max_length=11)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
   
    def __str__(self):
        return f'{self.nome}'
    
class Medico(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    crm = models.CharField(max_length=6)
    especialidade = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome}'
