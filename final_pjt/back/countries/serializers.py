from rest_framework import serializers
from .models import Country, Exchange, Comment, Travel

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', )

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        