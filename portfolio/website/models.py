from django.db import models

# Create your models here.


class Project (models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=1000)
    site = models.CharField(max_length=255)
    

    def __str__(self):
        return self.title

