from django.db import models

class Video(models.Model):
    MOVIE_CATEGORY_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('sci-fi', 'Science Fiction'),
        ('horror', 'Horror'),
    ]
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='images/')
    video_file = models.FileField(upload_to='videos/')
    category = models.CharField(max_length=20, choices=MOVIE_CATEGORY_CHOICES)
    def __str__(self):
        return self.title + ' ----- ' + self.category
