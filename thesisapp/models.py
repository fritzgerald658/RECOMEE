from django.db import models


class PredictionResult(models.Model):
    career_one = models.CharField(max_length=100, null=True)
    career_two = models.CharField(max_length=100, null=True)
    career_three = models.CharField(max_length=100, null=True)
    