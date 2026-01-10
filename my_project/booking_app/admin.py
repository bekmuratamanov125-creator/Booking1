from django.contrib import admin
from .models import *


class CityInline(admin.TabularInline):
    model = City
    extra = 1


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name',)
    inlines = [CityInline]


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('hotel_name', 'hotel_stars', 'city', 'country')
    list_filter = ('hotel_stars', 'city', 'country', 'service')
    inlines = [HotelImageInline]


class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'type', 'status', 'price', 'hotel')
    list_filter = ('type', 'status', 'hotel')
    inlines = [RoomImageInline]


admin.site.register(UserProfile)
admin.site.register(City)
admin.site.register(Service)
admin.site.register(Review)
admin.site.register(Booking)
