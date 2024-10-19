from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser ):
    contact_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]  # Display first 50 characters

class Report(models.Model):
    message = models.TextField()
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

class DarkMode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_dark_mode = models.BooleanField(default=False)