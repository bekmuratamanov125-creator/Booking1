from rest_framework import routers
from django.urls import path, include
from .views import (
    CountryViewSet, CityViewSet, ServiceViewSet,
    HotelDetailAPIView, HotelListAPIView, RoomListAPIView, RoomDetailAPIView,
    UserProfileViewSet, ReviewListAPIView, ReviewDetailAPIView, BookingViewSet
)

router = routers.DefaultRouter()
router.register('countries', CountryViewSet)
router.register('cities', CityViewSet)
router.register('services', ServiceViewSet)
router.register('users', UserProfileViewSet)
router.register('bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('hotel/', HotelListAPIView.as_view(), name='hotel-list'),
    path('hotel/ <int:pk>/', HotelDetailAPIView.as_view(), name='hotel-detail'),
    path('room/', RoomListAPIView.as_view(), name='room-list'),
    path('room/ <int:pk>/', RoomDetailAPIView.as_view(), name='room-detail'),
    path('review/', ReviewListAPIView.as_view(), name='review-list'),
    path('review/ <int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]
