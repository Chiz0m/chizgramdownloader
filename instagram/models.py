from django.db import models

# Create your models here.
class Instagram(models.Model):
    url = models.TextField()

    def __str__(self):
        return self.url
    