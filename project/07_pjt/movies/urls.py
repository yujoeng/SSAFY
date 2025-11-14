from django.urls import path
from . import views

urlpatterns = [
    # 배우
    path('actors/', views.actor_list),
    path('actors/<int:actor_id>/', views.actor_detail),

    

    # 영화
    path('movies/', views.movie_list),
    path('movies/<int:movie_id>/', views.movie_detail),

    # 특정 영화의 리뷰 목록/ 생성 

    path('reviews/', views.review_list),
    # path('reviews/<int:movie_id>/', views.review_list),
    path('reviews/<int:review_id>/', views.review_detail),
    # 개별 리뷰 조회/수정/삭제

    path('movies/<int:review_id>/reviews/', views.create_review),

]