from rest_framework import serializers
from .models import Ride, CustomUser, Staff, Student, Driver, Location, Payment, Wallet, Booking

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'role']
        read_only_fields = ['id', 'role']

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'user', 'dept', 'post']
        read_only_fields = ['id']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'matric_no', 'dept', 'faculty']
        read_only_fields = ['id']

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'user', 'vehicle_type', 'status', 'vehicle_num', 'licence_no']
        read_only_fields = ['id']

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['id', 'rider', 'origin_place', 'destination', 'status', 'option', 'start_time', 'end_time']
        read_only_fields = ['id', 'start_time', 'end_time']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'place_img', 'latitude', 'longitude']
        read_only_fields = ['id']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'ride', 'user', 'amount', 'payment_method', 'status']
        read_only_fields = ['id']

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'user', 'balance']
        read_only_fields = ['id']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['id', 'booked_date']
