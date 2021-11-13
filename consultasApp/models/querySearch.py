from django.db import models


class QuerySearch(models.Model):
    id = models.AutoField(primary_key=True)
    search = models.TextField(155, unique=True)
    amount = models.IntegerField(default=0)
    firstSearch = models.IntegerField()
    lastSearch = models.IntegerField()
    numberResults = models.IntegerField()
