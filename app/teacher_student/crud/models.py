from django.db import models


class Teachers(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Stars(models.Model):
    teachers = models.ForeignKey('Teachers', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['teachers']

    def __str__(self):
        return self.teachers


class Students(models.Model):
    name = models.CharField(max_length=50)
    # stars = models.ForeignKey('Teachers',
    #                           on_delete=models.CASCADE,
    #                           null=True,
    #                           related_name="teachers",
    #                           related_query_name="teacher")
    stars = models.ManyToManyField(Stars, null=True)
    teachers = models.ManyToManyField(Teachers, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

