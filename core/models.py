from django.db import models


class Session(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    diagram = models.TextField()
