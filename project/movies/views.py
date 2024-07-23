from django.shortcuts import render, get_object_or_404
from .models import Media


def movie_detail(request, pk):
    movie = get_object_or_404(Media, pk=pk)
    context = {
        'movie': movie
    }
    return render(request, 'movie_detail.html', context)
