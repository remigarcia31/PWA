from django.db import models

# Create your models here.

class AppTS(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title

class Items(models.Model):
    itm_name= models.CharField(max_length=120)
