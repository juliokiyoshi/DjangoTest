from rest_framework import serializers
from .models import Card 
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Card
        fields=('nome_Professor','ic','remunerada','data_encerramento','requisitos','assunto') 