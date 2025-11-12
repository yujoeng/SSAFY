from django.db import models

# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length=10, primary_key=True)
    author = models.TextField()
    title = models.TextField()

# 가독성 향상용 코드 입력 
    def __str__(self):
        return f'{self.title} ({self.author})'