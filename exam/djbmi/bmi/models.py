from django.db import models

# Create your models here.
class People(models.Model):
    photo = models.ImageField(upload_to='img/', blank=True, null=True)
    ssn = models.CharField(max_length=10)
    pname = models.CharField(max_length=30)
    tall = models.DecimalField(max_digits=4, decimal_places=1)
    weight = models.DecimalField(max_digits=4, decimal_places=1)
