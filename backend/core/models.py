from django.db import models

# Create your models here.


class Task(models.Model):

    title = models.CharField(max_length=128)
    due_date = models.DateField(blank=True)
    is_done = models.BooleanField(default=False)

    class Meta:
        unique_together = ['title', 'due_date']
