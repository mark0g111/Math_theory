from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.FileField(upload_to='tasks/files/', blank=True)

    def __str__(self):
        return self.title
