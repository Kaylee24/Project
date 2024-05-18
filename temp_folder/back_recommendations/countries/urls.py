from django.urls import path
from . import views

app_name='country'
urlpatterns = [
    # 실험 index url
    path('<int:pk>', views.index, name='index'),
    
    # main page에 들어갈 나라 사진
    path('main_country_picture/', views.main_country_picture),

    # comparison page
    path('comparison_page/', views.comparison_page),

    # detail page
    path('detail_page/', views.detail_page),

    # profile page
    path('profile_page/<int:user_pk>', views.profile_page),

    # 여행 추천을 위한 URL 추가
    path('recommendations/', views.travel_recommendations, name='travel_recommendations'),

]
