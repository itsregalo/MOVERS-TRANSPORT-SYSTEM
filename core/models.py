from django.db import models
from django.db.models.deletion import DO_NOTHING
from accounts.models import User
# Create your models here.


class VehicleCategory(models.Model):
    category_name = models.CharField(max_length=200)
    load_capacity = models.PositiveIntegerField()
    cost_per_km = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.category_name
    
class Vehicle(models.Model):
    vehicle_no = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    vehicle_category = models.ForeignKey(VehicleCategory, on_delete=DO_NOTHING)

    def __str__(self):
        return self.vehicle_no

class Driver(models.Model):
    user = models.ForeignKey(User, on_delete=DO_NOTHING)
    license_no = models.CharField(max_length=254)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    



