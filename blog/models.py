# Create your models to store post data here.
# each post will associated to a user, user model
# posts should not be deleted on category deletion
# posts should have timestamps

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
