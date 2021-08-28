from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(VehicleCategory)
admin.site.register(Vehicle)
admin.site.register(IndividualMembership)
admin.site.register(SmallScaleMembers)
admin.site.register(GroupMembership)
admin.site.register(Driver)