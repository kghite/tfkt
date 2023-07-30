from django.contrib.gis.db import models


class Named(models.Model):
    name = models.CharField(max_length=32, default=None, null=True)
    description = models.CharField(max_length=128, default=None, null=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
