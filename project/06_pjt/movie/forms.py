from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'director', 'genre', 'score']
        labels = {
            'title' : '제목',
            'description' : '줄거리',
            'director' : '감독',
            'genre' : '장르',
            'score' : '평점',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '10'}),
        }