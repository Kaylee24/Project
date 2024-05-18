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
    path('detail_page/<int:country_pk>/<int:user_pk>', views.detail_page),

    # detail page의 댓글 삭제 url
    path('detail_page/delete/<int:comment_pk>', views.comment_delete),

    # profile page
    path('profile_page/<int:user_pk>', views.profile_page),

    # 여행 추천을 위한 URL 추가
    path('recommendations/', views.travel_recommendations, name='travel_recommendations'),


]
