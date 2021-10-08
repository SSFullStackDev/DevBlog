from django.db import models

class price_history(models.Model):
    title = models.CharField(max_length=20)
    data = models.JSONField(default = [])

    def __str__(self):
        return self.title
