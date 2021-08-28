from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.


class VehicleCategory(models.Model):
    category_name = models.CharField(max_length=200)
    load_capacity = models.PositiveIntegerField()
    cost_per_km = models.DecimalField(decimal_places=2)

    def __str__(self):
        return self.category_name
    
class Vehicles(models.Model):
    vehicle_no = models.TextField(max_length=255)
    vehicle_category = models.ForeignKey(VehicleCategory, on_delete=DO_NOTHING)

    def __str__(self):
        return self.vehicle_no

class IndividualMembership(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=13)
    location = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SmallScaleMembers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class GroupMembership(models.Model):
    group_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    members = models.ManyToOneRel(SmallScaleMembers)

    def __str__(self):
        return self.group_name



