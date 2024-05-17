from django.urls import path
from . import views


urlpatterns = [
    # main page에 들어갈 나라 사진
    # 전체를 다 가져올거임
    path('main_country_picture/', views.main_country_picture),

    # # 이거 필요없을거 같은데?
    # # main page에 들어갈 여행 계획하기 form
    # path('main_travel/', views.main_travel)
]
