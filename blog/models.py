# Create your models to store post data here.
# each post will associated to a user, user model
# posts should not be deleted on category deletion
# posts should have timestamps

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
