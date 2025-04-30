from rest_framework import serializers
from .models import Ride, CustomUser, Staff, Student, Driver, Location,Payment,Wallet,Booking

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'role']
        read_only_fields = ['id', 'role']
        exclude = ['password']

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'user', 'dept', 'post']
        read_only_fields = ['id']
        extra_kwargs = {
            'user': {
                'required':True,
                'allow_blank':False
            },
            'dept': {
                'required':True,
                'allow_blank':False
            },
            'post': {
                'required':True,
                'allow_blank':False
            }
        }

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'matric_no', 'dept', 'faculty']
        read_only_fields = ['id']
        extra_kwargs = {
            'user': {
                'required':True,
                'allow_blank':False
            },
            'matric_no': {
                'required':True,
                'allow_blank':False
            },
            'dept': {
                'required':True,
                'allow_blank':False
            },
            'faculty': {
                'required':True,
                'allow_blank':False
            }
        }

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'user', 'vehicle_type', 'status','vehicle_num','licence_no']
        read_only_field = ['id']
        
class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['id', 'rider', 'origin_place', 'destination', 'status', 'option', 'start_time', 'end_time']
        read_only_fields = ['id','start_time','end_time']
        extra_kwargs = {
            'rider': {
                'required':True,
                'allow_blank':False
            },
            'origin_place': {
                'required':True,
                'allow_blank':False
            },
            'destination': {
                'required':True,
                'allow_blank':False
            },
            'status': {
                'required':True,
                'allow_blank':False
            },
            'option': {
                'required':True,
                'allow_blank':False
            }
        }

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'place_img', 'latitude', 'longitude']
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {
                'required':True,
                'allow_blank':False
            },
            'place_img': {
                'required':True,
                'allow_blank':False
            },
            'latitude': {
                'required':True,
                'allow_blank':False
            },
            'longitude': {
                'required':True,
                'allow_blank':False
            }
        }

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id','ride', 'user', 'amount', 'payment_method', 'status']
        read_only_fields = ['id']
        extra_kwargs = {
            'user': {
                'required':True,
                'allow_blank':False
            },
            'amount': {
                'required':True,
                'allow_blank':False
            },
            'payment_method': {
                'required':True,
                'allow_blank':False
            },
            'status': {
                'required':True,
                'allow_blank':False
            }
        }

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'user', 'balance']
        read_only_fields = ['id']
        extra_kwargs = {
            'user': {
                'required':True,
                'allow_blank':False
            },
            'balance': {
                'required':True,
                'allow_blank':False
            }
        }

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['id','booked_date']