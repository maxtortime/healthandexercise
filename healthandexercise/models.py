from django.contrib.auth.models import User
from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=128, blank=False, default='⭕')
    exerciser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    exercise_at = models.DateField(auto_now_add=True)
