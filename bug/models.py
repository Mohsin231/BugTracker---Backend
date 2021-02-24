from django.db import models

# Create your models here.
class Bug(models.Model):
    creator = models.CharField(max_length=100)
    details = models.TextField()
    steps = models.TextField()
    Priority = models.TextField()
    Time = models.TextField()
    # error_image = models.ImageField(null=True, blank=True, upload_to=)

    def __str__(self):
        return self.creator

# class User(models.Model):
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')