from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100) # 배우 이름 설정

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()
    actors = models.ManyToManyField(Actor, related_name= 'movies')

    def __str__(self):
        return self.title


class MovieActor(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    role = models.CharField(max_length=100, blank=True)

    class Meta:
        unique_together = ('movie', 'actor')
        
class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='reviews',   # 역참조를 위함 
    )
    title = models.CharField(max_length=100) # 리뷰 제목
    content = models.TextField()   # 리뷰 내용 

    def __str__(self):
        return self.title