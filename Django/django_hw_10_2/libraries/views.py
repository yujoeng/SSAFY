from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookListSerializer

@api_view(['GET'])
def book_list(request):
    qs = Book.objects.all().order_by('title')
    data = BookListSerializer(qs, many=True).data
    return Response(data)
