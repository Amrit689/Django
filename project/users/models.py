from django.db import models
from django.contrib.auth import get_user_model



class UserProfileModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="profile", null=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def has_profile_pic(self):
        return bool(self.profile_picture and hasattr(self.profile_picture, 'url'))
    
class MovieBooking(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    poster=models.ImageField()
    title=models.CharField(max_length=200)
    price=models.CharField(max_length=200)


