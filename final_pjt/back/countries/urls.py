from django.urls import path
from . import views


urlpatterns = [
    # main page에 들어갈 나라 사진
    path('main_country_picture/', views.main_country_picture),

    # comparison page
    path('comparison_page/', views.comparison_page),

    # detail page
    path('detail_page/', views.detail_page),

    # profile page
    path('profile_page/<int:user_pk>', views.profile_page),
]
