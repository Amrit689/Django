from django.shortcuts import render
from .models import Media

def home(request):
    recommended_movies = Media.objects.filter(category='Recommended')
    upcoming_movies = Media.objects.filter(category='Upcoming')
    live_movies = Media.objects.filter(category='Live')
    recommended_shows = Media.objects.filter(category='Show Recommended')
    upcoming_shows = Media.objects.filter(category='Show Upcoming')
    live_shows = Media.objects.filter(category='Show Live')

    context = {
        'recommended_movies': recommended_movies,
        'upcoming_movies': upcoming_movies,
        'live_movies': live_movies,
        'recommended_shows': recommended_shows,
        'upcoming_shows': upcoming_shows,
        'live_shows': live_shows,
    }

    return render(request, 'home.html', context)