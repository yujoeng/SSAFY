from rest_framework import serializers
from .models import Book

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']  # 목록은 제목만
