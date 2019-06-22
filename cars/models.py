from django.db import models

# Create your models here.
class Manufacturer(models.Model): 
    brand = models.CharField(max_length = 20)
    country = models.CharField(max_length = 30)

    def __str__(self):
        return self.brand

class Fuel(models.Model):
    type_fuel = models.CharField(max_length = 50)

    def __str__(self):
        return self.type_fuel

class Vehicle(models.Model):
    model = models.CharField(max_length = 50)
    color = models.CharField(max_length = 20)
    board = models.CharField(max_length = 7)
    chassis = models.CharField(max_length = 17)
    year = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE )
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE )
    


