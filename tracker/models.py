from django.db import models


class Measurement(models.Model):
    date = models.DateTimeField
    weight = models.DecimalField
    bodyFat = models.DecimalField


class Nutrition(models.Model):
    date = models.DateTimeField
    calories = models.IntegerField
    protein = models.IntegerField
    carbohydrates = models.IntegerField
    fat = models.IntegerField


class Exercise(models.Model):
    date = models.DateTimeField
    description = models.CharField(max_length=128)
    type = models.CharField(max_length=50)
    minutes = models.IntegerField
    calories = models.IntegerField
