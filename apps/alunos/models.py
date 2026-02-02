from django.db import models
from django.conf import settings

class Aluno(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('trancado', 'Trancado'),
        ('formado', 'Cancelado'),
    ]

    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'aluno')
    matricula = models.CharField(max_length = 20, unique = True)
    cpf = models.CharField(max_length = 11, unique = True)
    data_nascimento = models.DateField()
    data_ingresso = models.DateField(auto_now_add = True)
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = 'ativo')
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
    
    def __str__(self):
        return f"{self.matricula} - {self.usuario.get_full_name()}"