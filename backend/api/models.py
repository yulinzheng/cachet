from django.db import models


class Note(models.Model):
    title = models.TextField(null=True, blank=True)
    body = models.TextField(null=True)
    url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.body[0:500]
