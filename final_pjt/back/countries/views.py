from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from .models import Comment, Country, Travel
from .serializers import ComparisonCountrySerializer, MainCountryPictureSerializer, ProfileSerializer, CommentCreateSerializer, DetailCountrySerializer
from rest_framework import status

@api_view(['GET'])
def main_country_picture(request):
    countries = Country.objects.all()
    serializer = MainCountryPictureSerializer(countries, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def comparison_page(request):
    countries = Country.objects.all()
    serializer = ComparisonCountrySerializer(countries, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def detail_page(request, country_pk):
    country = get_object_or_404(Country, pk=country_pk)
    if request.method == 'GET':
        serializer = DetailCountrySerializer(country)
        return Response(serializer.data)
    elif request.method == 'POST':
        if request.user.is_authenticated:
            serializer = CommentCreateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(country_c=country, user=request.user)
                print(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def profile_page(request, username):
    profile = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)

def index(request, pk):
    countries = get_object_or_404(Country, pk=pk)
    context = {
        'countries' : countries,
    }
    return render(request, 'index.html', context)

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

@api_view(['GET'])
def search_country(request):
    query = request.query_params.get('q', '')
    try:
        country = Country.objects.get(name__icontains=query)
        serializer = ComparisonCountrySerializer(country)
        return Response(serializer.data)
    except Country.DoesNotExist:
        return Response({'error': 'Country not found'}, status=status.HTTP_404_NOT_FOUND)





# visited, interested

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def update_visited_countries(request):
#     user = request.user
#     country_ids = request.data.get('country_ids', [])
#     countries = Country.objects.filter(id__in=country_ids)
#     user.visited.set(countries)
#     user.save()
#     return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def update_interested_countries(request):
#     user = request.user
#     country_ids = request.data.get('country_ids', [])
#     countries = Country.objects.filter(id__in=country_ids)
#     user.interested.set(countries)
#     user.save()
#     return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_visited_countries(request):
    user = request.user
    country_ids = request.data.get('country_ids', [])
    countries = Country.objects.filter(id__in=country_ids)
    for country in countries:
        user.visited.add(country)
    user.save()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_interested_countries(request):
    user = request.user
    country_ids = request.data.get('country_ids', [])
    countries = Country.objects.filter(id__in=country_ids)
    for country in countries:
        user.interested.add(country)
    user.save()
    return Response(status=status.HTTP_204_NO_CONTENT)
