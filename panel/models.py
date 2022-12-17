from django.db import models

# Create your models here.
class Iteam(models.Model):
    title = models.CharField(max_length=200)