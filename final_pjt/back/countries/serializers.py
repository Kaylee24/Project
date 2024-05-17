from rest_framework import serializers
from .models import Country, Exchange, Comment, Travel
from accounts.serializers import UserSerializer

# main_page에 들어갈 serializer
# 나라 사진 -> 전체를 다 가져올거임
class MainCountryPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('image', 'name')


# Country에서 역참조로 찾을 환율정보
class ExchangeGraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = ('code', 'rate', 'graph')

# comparison_page에 들어갈 serializer

# 나라에 대한 정보
class ComparisonCountrySerializer(serializers.ModelSerializer):

    
    exchange_set = ExchangeGraphSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['name', 'burger', 'coffee', 'area', 'image', 'exchange_set']


# detail_page에 들어갈 serializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'content')

class DetailCountrySerializer(serializers.ModelSerializer):

    comment_set = CommentSerializer(many=True, read_only=True)

    exchange_set = ExchangeGraphSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['name', 'burger', 'coffee', 'area', 'image', 'info', 'exchange_set', 'comment_set']

## nav바를 따로 serializer로 만들 필요는 없긴함
# 로그인 정보는 accounts에 있을듯?
# 그걸 가지ㅗㄱ 할듯