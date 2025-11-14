from rest_framework import serializers
from .models import Movie, Actor, Review

# class ActorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Actor
#         fields = ['id', 'name']   # 전체 배우 목록 배우의 id랑 name 만 요구함 
# 배우 목록용 
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name']


# 배우 상세용
class ActorDetailSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()
    
    class Meta:
        model =Actor
        fields = ['id', 'name', 'movies']

    def get_movies(self, obj):
        # 배우가 출연한 영화 제목 리스트
        return [movie.title for movie in obj.movies.all()]
        
        
# 영화 목록용 
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview')

# 영화 상세용
class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorListSerializer(many=True, read_only=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'overview',
            'release_date',
            'poster_path',
            'actors',
            'reviews',
        ]

    def get_reviews(self, obj):
        # 해당 영화에 달린 리뷰 제목/ 내용 목록 확인
        return[
            {
                'title': review.title,
                'content' : review.content, 
            }
            for review in obj.reviews.all()
        ]
    

# class MovieSerializer(serializers.ModelSerializer):
#     actors = ActorSerializer(many=True, read_only=True)

#     class Meta:
#         model = Movie
#         fields = '__all__'



# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = '__all__'
#         read_only_fields = ('movie',)

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'title', 'content']

# 리뷰 상세용
class ReviewDetailSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'movie', 'movie_title', 'title', 'content']
    
# 리뷰 생성용
class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['title', 'content']
