from rest_framework import serializers
from .models import Country, City, Service, Hotel, HotelImage, Room, RoomImage, UserProfile, Review, Booking

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CountryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name',]

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class CityNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name',]

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['service_name', 'service_image']

class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image',]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class HotelListSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializer(many=True, read_only=True)
    country = CountryNameSerializer()
    city = CityNameSerializer()
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_image', 'hotel_name', 'city', 'country']

class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id',  'room_number', 'type',
                  'status', 'price', 'room_description']


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializer(many=True, read_only=True)
    country = CountryNameSerializer()
    city = CityNameSerializer()
    service = ServiceSerializer(many=True)
    owner = UserProfileNameSerializer()
    hotel_room = RoomListSerializer(many=True, read_only=True)
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'hotel_image', 'city', 'country', 'postal_code', 'street',
                  'hotel_stars', 'description', 'service', 'owner', 'hotel_room']

class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image',]


class RoomDetailSerializer(serializers.ModelSerializer):
    room_image = RoomImageSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['id', 'room_image', 'room_number', 'type',
                  'status', 'price', 'room_description']


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text']

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'hotel', 'text', 'rating', 'created_date']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
