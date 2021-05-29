from django.db import models


class Teachers(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Students(models.Model):
    name = models.CharField(max_length=50, unique=True)
    teachers = models.ManyToManyField(Teachers, null=True)
    stars = models.ManyToManyField(
        Teachers,
        related_name="teachers",
        related_query_name="stars",
        null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
