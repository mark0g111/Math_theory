from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=100)
    description = models.FileField(blank=True)
