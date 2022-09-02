from django.db import models

# Create your models here.

class Disease(models.Model):
    name=models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Symptom(models.Model):
    body=models.CharField(max_length=500)

    def __str__(self):
        return self.body[0:50]
