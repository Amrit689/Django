from django.db import models

class Media(models.Model):
    CATEGORY_CHOICES = [
        ('Recommended', 'Recommended'),
        ('Upcoming', 'Upcoming'),
        ('Live', 'Live'),
        ('Show Recommended', 'Show Recommended'),
        ('Show Upcoming', 'Show Upcoming'),
        ('Show Live', 'Show Live'),
    ]

    title = models.CharField(max_length=100)
    release_year = models.DateField()
    genre = models.CharField(max_length=50)
    description = models.TextField()
    poster = models.ImageField(upload_to='media_posters/')
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    language=models.CharField(max_length=250)
    duration=models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
   

    def __str__(self):
        return self.title


class Review(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    reviewer = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return f'Review for {self.media.title} by {self.reviewer}'