from django.urls import path
from . import views

urlpatterns = [
    path('v1/libraries/', views.book_list, name='book-list'),
]
