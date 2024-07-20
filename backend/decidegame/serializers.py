# converting models to JSON
from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game #model to work with
        fields = ('id', 'title', 'summary') #fields to convert

class IdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id']
