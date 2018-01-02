from django.db import models

class Item(models.Model):
    topic=models.CharField(max_length=100)
    description=models.CharField(max_length=500)


class marks(models.Model):
    rollno=models.CharField(max_length=15)
    marks=models.CharField(max_length=200)
