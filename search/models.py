from django.db import models

class Query(models.Model):
    query = models.CharField(max_length=200)
