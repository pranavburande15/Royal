from django.contrib import admin
from .models import Bike, TextRiderBooking, BikeVariant

# Register your models here.

admin.site.register(Bike)
admin.site.register(TextRiderBooking)
admin.site.register(BikeVariant)
admin.site.site_header = "Royal Enfield Showroom Admin"
admin.site.site_title = "Royal Enfield Portal"
admin.site.index_title = "Welcome to Royal Enfield Management System"
