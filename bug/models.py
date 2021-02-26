from django.db import models

# Create your models here.
class Bug(models.Model):
    name = models.CharField(max_length=100, default="name of bug")
    priority = models.CharField(max_length=100, default="level of priority")
    details = models.TextField()
    steps = models.TextField()
    operating_system = models.CharField(max_length=100, default="computer system")
    assignee = models.CharField(max_length=100, default="assign a user to fix the bug")
    resolved = models.BooleanField(default=False)
    # error_image = models.ImageField(null=True, blank=True, upload_to=)

    def __str__(self):
        return self.name

# class User(models.Model):
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')