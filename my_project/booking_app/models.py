from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Country(models.Model):
    country_name = models.CharField(max_length=100)
    country_image = models.ImageField(upload_to='country_image', null=True, blank=True)

    def __str__(self):
         return self.country_name


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(80)],
                                           null=True, blank=True)
    user_image  = models.ImageField(upload_to='user_image', null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    RoleChoices = (
    ('owner', 'Owner'),
    ('client', 'Client'),
    )
    role = models.CharField(max_length=10, choices=RoleChoices, default='client')
    data_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.role}'


class City(models.Model):
    city_name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    city_image = models.ImageField(upload_to='city_image', null=True, blank=True)

    def __str__(self):
        return self.city_name


class Service(models.Model):
    service_name = models.CharField(max_length=100, unique=True)
    service_image = models.ImageField(upload_to='service_image', null=True, blank=True)

    def __str__(self):
        return self.service_name


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    postal_code = models.PositiveSmallIntegerField()
    street = models.CharField(max_length=100)
    hotel_stars = models.PositiveSmallIntegerField(choices=[(i,str(i)) for i in range(1,11)])
    description = models.TextField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.hotel_name


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_image')
    hotel_image = models.ImageField(upload_to='hotel_image', null=True, blank=True)



class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_room')
    room_number = models.IntegerField()
    TypeChoices = (
        ('luxury', 'Luxury'),
        ('junior suite', 'Junior suite'),
        ('economy', 'Economy'),
        ('family', 'Family'),
        ('single', 'Single'),
    )
    type = models.CharField(max_length=100, choices=TypeChoices, default='single')
    StatusChoices = (
        ('booked', 'booked'),
        ('free', 'Free'),
        ('busy', 'Busy'),
    )
    status = models.CharField(max_length=100, choices=StatusChoices, default='free')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    room_description = models.TextField()

    def __str__(self):
        return str(self.room_number)


class RoomImage(models.Model):
   room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_image')
   room_image = models.ImageField(upload_to='room_image', null=True, blank=True)


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(choices=[(i,str(i)) for i in range(1,11)])
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating} {self.user.username} {self.hotel.hotel_name}'


class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return  f'{self.user} {self.hotel} {self.room}'


