from django.db import models

class Bookmark(models.Model):
    title = models.CharField(max_length=255, null=False)
    url = models.URLField(max_length=1024, null=False)
    notes = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
