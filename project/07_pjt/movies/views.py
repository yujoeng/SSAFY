from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Actor, Movie, Review
from .serializers import (
    # ActorSerializer,
    ActorListSerializer,
    ActorDetailSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    # ReviewSerializer,
    ReviewListSerializer,
    ReviewDetailSerializer,
    ReviewCreateSerializer,
)


# Create your views here.
    # 배우 목록 / 상세 
@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)

# 단일 배우 + 출연 영화 제목 
@api_view(['GET'])
def actor_detail(request, actor_id):
    actor = get_object_or_404(Actor, pk=actor_id)
    serializer = ActorDetailSerializer(actor)
    return Response(serializer.data)

# 영화 목록 / 생성
@api_view(['GET'])
def movie_list(request):
    # if request.method == 'GET':
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    
# 영화 상세 
@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

# 전체 영화의 리뷰 목록
@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
    
# 리뷰 단일 조회 수정 삭제 
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'GET':
        serialzer = ReviewDetailSerializer(review)
        return Response(serialzer.data)
    
    elif request.method == 'PUT':
        serialzer = ReviewDetailSerializer(review, data=request.data)
        if serialzer.is_valid(raise_exception=True):
            serialzer.save()
            detail_serializer = ReviewDetailSerializer(review)
            return Response(serialzer.data)
        return Response(serialzer.errors, status=status.HTTP_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_review(request, movie_id):
    movie =get_object_or_404(Movie, pk=movie_id)

    serializer = ReviewCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)