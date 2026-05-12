from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    salary = models.IntegerField()

    def __str__(self):
        return self.name
