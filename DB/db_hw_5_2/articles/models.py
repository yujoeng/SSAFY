# articles/models.py
from django.db import models
from django.conf import settings

class Article(models.Model):
    # 작성자: User 1:N Article
    # 역참조 매니저 : user.articles
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles'
    )

    # 좋아요 : User M:N Article
    # 역참조 매니저 : user.like_articles
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_articles',
        blank=True
    )

    # ERD 컬럼
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.title}'