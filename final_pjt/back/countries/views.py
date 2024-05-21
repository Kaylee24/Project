from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from .models import Comment, Country, Travel
from .serializers import ComparisonCountrySerializer, MainCountryPictureSerializer, ProfileSerializer, CommentCreateSerializer
from rest_framework import status

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
# def detail_page(request, country_pk, user_pk):
def detail_page(request, country_pk):
    # country = Country.objects.get(pk=country_pk)
    country = get_object_or_404(Country, pk=country_pk)
    if request.method == 'GET':
        serializer = ComparisonCountrySerializer(country)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        if request.user.is_authenticated:
            serializer = CommentCreateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(country_c=country, user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    # if request.method == 'DELETE':
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def profile_page(request, user_pk):
    # profile = User.objects.get(pk=user_pk)
    profile = get_object_or_404(User, pk=user_pk)
    serializer = ProfileSerializer(profile, many=True)
    return Response(serializer.data)

# 데이터 나오는지 확인용
def index(request, pk):
    # countries = Country.objects.get(pk=pk)
    countries = get_object_or_404(Country, pk=pk)
    context = {
        'countries' : countries,
    }
    return render(request, 'index.html', context)


# @api_view(['POST', 'GET'])
# def travel_recommendations(request):
#     if request.method == 'POST':
#         desired_country = request.POST.get('country')
#         budget = float(request.POST.get('budget'))
#         days = int(request.POST.get('days'))

#         try:
#             country = Country.objects.get(name=desired_country)
#         except Country.DoesNotExist:
#             return Response({'error': 'Country not found'}, status=404)

#         area_countries = Country.objects.filter(area=country.area)
#         recommendations = []

#         daily_budget = budget / days

#         for c in area_countries:
#             total_cost_per_day = (c.burger + c.coffee) * c.rate
#             daily_cost_index = daily_budget / total_cost_per_day

#             if daily_cost_index < 3:
#                 style = 'Not recommended'
#             elif 3 <= daily_cost_index < 6:
#                 style = 'Backpacker'
#             elif 6 <= daily_cost_index < 10:
#                 style = 'Mid-range'
#             else:
#                 style = 'Luxury'

#             recommendations.append({
#                 'country': c.name,
#                 'travel_style': style,
#                 'cost_index': daily_cost_index
#             })

#         return render(request, 'recommendations.html', {'recommendations': recommendations})

#     return render(request, 'recommendations.html')


@api_view(['POST'])
def travel_recommendations(request):
    desired_country = request.data.get('country')
    budget = float(request.data.get('budget'))
    days = int(request.data.get('days'))

    try:
        country = Country.objects.get(name=desired_country)
    except Country.DoesNotExist:
        return Response({'error': 'Country not found'}, status=404)

    area_countries = Country.objects.filter(area=country.area)
    recommendations = []

    daily_budget = budget / days

    for c in area_countries:
        total_cost_per_day = (c.burger + c.coffee) * c.rate
        daily_cost_index = daily_budget / total_cost_per_day

        if daily_cost_index < 3:
            style = 'Not recommended'
        elif 3 <= daily_cost_index < 6:
            style = 'Backpacker'
        elif 6 <= daily_cost_index < 10:
            style = 'Mid-range'
        else:
            style = 'Luxury'

        recommendations.append({
            'country': c.name,
            'travel_style': style,
            'cost_index': daily_cost_index
        })

    return Response({'recommendations': recommendations})