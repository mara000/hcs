from django.db import models

# Create your models here.
class Participant(models.Model):
  firstname = models.CharField(max_length=255)
  password = models.CharField(max_length=255)