from django.db import models

# Create your models here.
class Task(models.Model):
    task_text = models.CharField(max_length=150)
    task_status = models.CharField(max_length=10)