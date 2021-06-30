from django.db import models

# Create your models here.
class Card(models.Model):
    nome_Professor=models.CharField(default="",max_length=255)
    ic=models.CharField(default="",max_length=255)
    remunerada=models.BooleanField(null=False,default=False)
    data_encerramento=models.CharField(default="",max_length=10)
    requisitos=models.BooleanField(null=False,default=False)
    assunto=models.CharField(default="",max_length=255)
