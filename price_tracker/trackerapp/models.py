from django.db import models

class price_history(models.Model):
    title = models.CharField(max_length=100)
    data = models.JSONField(default=dict)

#    def __str__(self):
 #       return self.title
