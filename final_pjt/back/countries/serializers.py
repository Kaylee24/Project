from rest_framework import serializers
from .models import Country, Comment, Travel
from accounts.models import User
from accounts.serializers import UserSerializer

# main_page에 들어갈 serializer
# 나라 사진 -> 전체를 다 가져올거임
class MainCountryPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'image1', 'name')

# comparison_page에 들어갈 serializer
# 나라에 대한 정보
class ComparisonCountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['id', 'name', 'burger', 'coffee', 'area', 'image1', 'code', 'rate', 'graph']


# detail_page에 들어갈 serializer

# 이거는 나중에 profile_page에서도 쓸거임
class CommentSerializer(serializers.ModelSerializer):
    class CommentUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('name',)

    user = CommentUserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('user', 'content', 'created_at',)

class DetailCountrySerializer(serializers.ModelSerializer):

    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'burger', 'coffee', 'area', 'image1', 'image2', 'image3', 'code', 'rate', 'graph', 'comment_set']


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('content', 'created_at', 'user')
        read_only_fields = ('user', 'country_c')

# profile page에 들어갈 serializer

class ProfileCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'image1')

class ProfileSerializer(serializers.ModelSerializer):

    # detail_page에서 썼던 CommentSerializer 가져옴
    comment_set = CommentSerializer(source='comment_set', many=True, read_only=True)

    visited = ProfileCountrySerializer(many=True, read_only=True)
    interested = ProfileCountrySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('name', 'gender', 'age', 'visited', 'interested', 'comment_set')



## nav바를 따로 serializer로 만들 필요는 없긴함
# 로그인 정보는 accounts에 있을듯?
# 그걸 가지고 할듯