from django.db import models
from django.contrib.auth import get_user_model

CHOICE_NIVEL = [(1, 1),
                (3,3),
                (5,5),
                (8,8)]


CHOICE_PRIORIDADE = [(1, 1),
                     (2,2),
                     (3,3)]

User = get_user_model()

class Task(models.Model):

    descricao = models.CharField(max_length=200, blank=True, default='')
    responsavel = models.CharField(max_length=250, blank=True, default='')
    nivel = models.IntegerField(choices=CHOICE_NIVEL)
    situacao = models.CharField(max_length=12)
    prioridade = models.IntegerField(choices=CHOICE_PRIORIDADE)
    usuario = models.ForeignKey(
        User, related_name='tasks', on_delete=models.SET_NULL, null=True, default=None)
