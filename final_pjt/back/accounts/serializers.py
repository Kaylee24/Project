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

# class SignUpUserSerializer(serializers.ModelSerializer):
#     password1 = serializers.CharField(write_only=True)
#     password2 = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2', 'name', 'gender', 'age']

#     def validate(self, data):
#         if data['password1'] != data['password2']:
#             raise serializers.ValidationError("Passwords do not match")
#         return data

#     def create(self, validated_data):
#         user = User(
#             username=validated_data['username'],
#             name=validated_data['name'],
#             gender=validated_data['gender'],
#             age=validated_data['age']
#         )
#         user.set_password(validated_data['password1'])
#         user.save()
#         return user

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User


class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(
      required=False,
      allow_blank=True,
      max_length=255
    )
    gender = serializers.CharField(
      required=False,
      allow_blank=True,
      max_length=255
    )
    age = serializers.CharField(
      required=False,
      allow_blank=True,
      max_length=255
    )
    email = serializers.CharField(
        required=False,
      allow_blank=True,
      max_length=255
    )

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'name': self.validated_data.get('name', ''),
            'gender': self.validated_data.get('gender', ''),
            'age': self.validated_data.get('age', ''),
            'email' : self.validated_data.get('email', '')
        }