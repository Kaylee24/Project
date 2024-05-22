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
    # path('detail_page/<int:country_pk>/<int:user_pk>', views.detail_page),
    path('detail_page/<int:country_pk>', views.detail_page),

    # detail page의 댓글 삭제 url
    path('detail_page/delete/<int:comment_pk>', views.comment_delete),

    # profile page
    path('profile_page/<str:username>', views.profile_page),

    # 여행 추천을 위한 URL 추가
    path('recommendations/', views.travel_recommendations, name='travel_recommendations'),

    # detail page 검색을 위한 URL 추가
    path('search_country/', views.search_country, name='search_country'),



    # visited, interested

    path('update_visited_countries/', views.update_visited_countries, name='update_visited_countries'),
    path('update_interested_countries/', views.update_interested_countries, name='update_interested_countries'),
]
