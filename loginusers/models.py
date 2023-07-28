from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=False)

    # Add related_name to auth.User.groups field
    groups = models.ManyToManyField('auth.Group', related_name='auth_user_groups', blank=True)

    # Add related_name to auth.User.user_permissions field
    user_permissions = models.ManyToManyField('auth.Permission', related_name='auth_user_permissions', blank=True)

    def __str__(self):
        return self.username
