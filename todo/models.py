from django.db import models

# Create your models here.

class List(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=30)

    def __str__(self):
        return self.id