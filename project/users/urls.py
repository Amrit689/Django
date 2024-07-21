from .views import login_view,signup_view,logout_view,home_view,profile_view,update_user_profile
from django.urls import path

urlpatterns = [
    path('login/',login_view,name="login_view"),
    path('signup/',signup_view,name="signup_view"),
    path('logout/',logout_view,name="logout_view"),  # Logout view
    path('home/', home_view, name="home_view"),
    path('profile/<str:username>/', profile_view, name="profile_view"),  
    path('update_user/', update_user_profile, name="update_user_profile"),  # Update user profile view  # Update user profile view  # Update user profile view  # Update user profile view  # Update user profile view  # Update user profile view  # Update user profile view  # Update user profile view  # Update user profile view  # Update user profile view  # Update user profile view  # Update user profile view  # Update user profile view  #
    
]