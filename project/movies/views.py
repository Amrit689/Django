from django.shortcuts import render, get_object_or_404, redirect
from .models import Media

def movie_detail(request, pk):
    movie = get_object_or_404(Media, pk=pk)
    context = {
        'movie': movie
    }
    return render(request, 'movie_detail.html', context)

def book_tickets(request, pk):
    movie = get_object_or_404(Media, pk=pk)
    context = {
        'movie': movie
    }
    return render(request, 'book_tickets.html', context)

def confirm_booking(request, pk):
    if request.method == 'POST':
        movie = get_object_or_404(Media, pk=pk)
        theater = request.POST.get('theater')
        time = request.POST.get('time')
        price = request.POST.get('price')

        # Store booking information in session
        if 'bookings' not in request.session:
            request.session['bookings'] = []
        
        request.session['bookings'].append({
            'movie_title': movie.title,
            'theater': theater,
            'time': time,
            'price': price
        })
        request.session.modified = True  # Mark the session as modified

        # Redirect to the profile page or another appropriate page
        return redirect('profile_view', username=request.user.username)

    return render(request, 'book_tickets.html', {'movie': get_object_or_404(Media, pk=pk)})
