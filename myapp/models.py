from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.title}'
