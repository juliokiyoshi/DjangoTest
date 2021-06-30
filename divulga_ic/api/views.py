from django.shortcuts import render
from rest_framework import generics
from .serializers import CardSerializer
from .models import Card
from rest_framework.response import Response

class CardView(generics.CreateAPIView):
    queryset=Card.objects.all()
    serializer_class= CardSerializer 

def cardList(request):
    event=Card.objects.all()
    serializer=CardSerializer(event,many=True)
    return Response(serializer.data)

