from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


