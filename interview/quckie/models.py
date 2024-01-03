from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core.validators import MinValueValidator


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    due_date = models.DateField(default=timezone.now(),
    validators=[MinValueValidator(limit_value=timezone.now())],

        ) 

    def __str__(self):
        return self.title 
