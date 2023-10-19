from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='images/')
    video_file = models.FileField(upload_to='videos/')
