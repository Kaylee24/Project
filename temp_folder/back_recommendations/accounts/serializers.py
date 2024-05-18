# accounts/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
# from countries.serializers import CountrySerializer  # 주석 처리 또는 제거

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    visited = serializers.SerializerMethodField()
    interested = serializers.SerializerMethodField()

    def get_visited(self, obj):
        # 방문한 국가 데이터를 가져오는 메서드
        # 여기서 필요한 필드만 가져오거나 CountrySerializer를 사용하지 않고 직접 필요한 데이터를 가져와서 반환할 수 있습니다.
        return [country.name for country in obj.visited.all()]

    def get_interested(self, obj):
        # 관심 있는 국가 데이터를 가져오는 메서드
        # 여기서 필요한 필드만 가져오거나 CountrySerializer를 사용하지 않고 직접 필요한 데이터를 가져와서 반환할 수 있습니다.
        return [country.name for country in obj.interested.all()]

    class Meta:
        model = User
        fields = ['id', 'name', 'gender', 'age', 'visited', 'interested']
