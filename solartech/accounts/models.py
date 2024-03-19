from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    energy_production_data = models.FloatField(default=0.0)
    preferences = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
