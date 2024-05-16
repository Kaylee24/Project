from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page),
    path('articles/<int:article_pk>/', views.article_detail),
]
