from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Custom User model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
    )

# Post model
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]

# Report model
class Report(models.Model):
    message = models.TextField()
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# DarkMode model
class DarkMode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_dark_mode = models.BooleanField(default=False)

# Intermediate models for Groups and Permissions
class UserGroups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class UserUserPermissions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
