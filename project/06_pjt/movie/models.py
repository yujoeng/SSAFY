from django.db import models

# Create your models here.
class Movie(models.Model):
    GENRE_CHOICES = [
        ('Action', '액션'),
        ('Comedy', '코미디'),
        ('Drama', '드라마'),
        ('Horror', '공포'),
        ('Romance', '로맨스'),
        ('Sci-Fi', 'SF'),
        ('Thriller', '스릴러'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    director = models.CharField(max_length = 100)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title