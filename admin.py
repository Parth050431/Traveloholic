from django.contrib import admin
from django.db import models
from .models import Amenities, Hotel, Package, Extras, HotelBooking, Client, Contact

# Register your models here.


# Register your models here.
admin.site.register(Amenities)
admin.site.register(Hotel)
admin.site.register(Extras)
admin.site.register(Package)
admin.site.register(HotelBooking)
admin.site.register(Contact)
admin.site.register(Client)
