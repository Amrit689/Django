from django.urls import path
from . import views

urlpatterns = [
    path('movie_detail/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('book_tickets/<int:pk>/', views.book_tickets, name='book_tickets'),
    path('confirm_booking/<int:pk>/', views.confirm_booking, name='confirm_booking'),
]
