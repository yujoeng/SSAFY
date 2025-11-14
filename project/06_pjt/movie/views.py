from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movies = Movie.objects.all().order_by('-created_at')
    context = {
        'movies': movies,
    }
    return render(request, 'movie/index.html', context)

@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movie:detail', movie.pk)
    else:
        form = MovieForm()
    
    context = {
        'form': form,
    }
    return render(request, 'movie/create.html', context)

def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movie/detail.html', context)

@require_http_methods(["GET", "POST"])
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movie/update.html', context)

@require_POST
def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('movie:index')