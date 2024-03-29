from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    name: str = models.CharField(null=True, blank=True, max_length=100)
    age: int = models.IntegerField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['-name']),
        ]

    def __str__(self):
        return self.username
