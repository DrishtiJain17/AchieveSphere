from django.db import models

# Create your models here.
class College(models.Model):
    collegeName = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    collegeCode = models.IntegerField()

    def __str__(self):
        return self.collegeName