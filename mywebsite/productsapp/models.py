from django.db import models

# Create your models here.
class Product(models.Model):
    prid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
