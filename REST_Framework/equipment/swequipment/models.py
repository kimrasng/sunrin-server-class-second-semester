from django.db import models

class Equipment(models.Model):
    eid = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=100)
    type = models.TextField(max_length=100)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    location = models.TextField(max_length=100)