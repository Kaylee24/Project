from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from accounts.models import User
from .models import Comment, Country, Exchange, Travel
from .serializers import ComparisonCountrySerializer, MainCountryPictureSerializer, ProfileSerializer

@api_view(['GET'])
def main_country_picture(request):
    countries = Country.objects.all()
    # many=True는 Serialize 대상이 QuerySet인 경우 입력
    serializer = MainCountryPictureSerializer(countries, many=True)
    # data : Serialized data 객체에서 실제 데이터를 추출
    return Response(serializer.data)

@api_view(['GET'])
def comparison_page(request):
    countries = Country.objects.all()
    serializer = ComparisonCountrySerializer(countries, many=True)
    return Response(serializer.data)

# 여기서 댓글을 달게 할거라서 POST도 필요할듯?
# 수정필요 -> POST관련, 분기 나누기 등
@api_view(['GET', 'POST'])
def detail_page(request):
    countries = Country.objects.all()
    serializer = ComparisonCountrySerializer(countries, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def profile_page(request, user_pk):
    profile = User.objects.get(pk=user_pk)
    serializer = ProfileSerializer(profile, many=True)
    return Response(serializer.data)