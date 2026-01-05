from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name
