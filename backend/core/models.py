from django.db import models

# Create your models here.


class Task(models.Model):

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(blank=True)
    is_done = models.BooleanField(default=False)

    class Meta:
        unique_together = ['name', 'due_date']
