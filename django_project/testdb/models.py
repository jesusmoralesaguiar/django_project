from django.db import models


class Cities(models.Model):
    name = models.CharField(max_length=80)
    country = models.CharField(max_length=50)
    population = models.IntegerField()
    area = models.IntegerField()


