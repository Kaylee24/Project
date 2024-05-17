from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Comment, Country, Exchange, Travel
from .serializers import CountrySerializer, CountryPictureSerializer

@api_view(['GET'])
def main_country_picture(request):
    countries = Country.objects.all()
    # many=True는 Serialize 대상이 QuerySet인 경우 입력
    serializer = CountryPictureSerializer(countries, many=True)
    # data : Serialized data 객체에서 실제 데이터를 추출
    return Response(serializer.data)
