from rest_framework import serializers
from .models import Country, Exchange, Comment, Travel
from accounts.serializers import UserSerializer

# main_page에 들어갈 serializer
# 나라 사진 -> 전체를 다 가져올거임
class CountryPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('image', 'name')

# 여행 계획 form
class TravelFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = ('country_t', 'budget', 'period')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    country_c = CountrySerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class ExchangeSerializer(serializers.ModelSerializer):
    country_e = CountrySerializer(read_only=True)

    class Meta:
        model = Exchange
        fields = '__all__'


class TravelSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    country_t = CountrySerializer(many=True, read_only=True)

    class Meta:
        model = Travel
        fields = '__all__'
