from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Exercise(models.Model):
    name = models.CharField(max_length=1, blank=False, default='⭕')
    exerciser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    exercise_at = models.DateField(default=now, null=False, blank=False)
