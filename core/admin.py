from django.contrib import admin
from core.models import *

# Register your models here..
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone','role']
    search_fields = ['first_name','last_name','role','phone']
    list_filter = ['role']
    ordering = ['-id']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'matric_no', 'dept', 'faculty']
    search_fields = ['user__first_name','user__last_name','matric_no','dept']
    list_filter = ['dept']
    ordering = ['-id']
    list_select_related = ['user']

    def fullname(self,obj):
        if obj.user:
            return f'{obj.user.first_name} {obj.user.last_name}'
        return "N/A"
    fullname.short_description = 'Full Name'


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'dept', 'post']
    search_fields = ['user__first_name','user__last_name','dept','post']
    list_filter = ['dept']
    ordering = ['-id']
    list_select_related = ['user']

    def fullname(self,obj):
        if obj.user:
            return f'{obj.user.first_name} {obj.user.last_name}'
        return "N/A"
    fullname.short_description = 'Full Name'

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ['rider_name', 'origin_place', 'destination','status']
    list_filter = ['status','option']
    search_fields = ['rider__user__first_name','rider__user__last_name', 'status']
    readonly_fields = ['start_time', 'end_time']
    ordering = ['-id']
    list_select_related = ['rider__user']
    
    def rider_name(self,obj):
        if obj.rider:
            return f'{obj.rider.user.first_name} {obj.rider.user.last_name}'
        return "N/A"
    rider_name.short_description =  'Rider Name'

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email_address', 'status','vehicle_type']
    search_fields = ['user__first_name','user__last_name','vehicle_type']
    list_filter = ['status','vehicle_type']
    ordering = ['-id']
    list_select_related = ['user']

    def fullname(self,obj):
        if obj.user:
            return f'{obj.user.first_name} {obj.user.last_name}'
        return "N/A"
    fullname.short_description = 'Full Name'

    def email_address(self,obj):
        if obj.user:
            return f'{obj.user.email}'
        return "N/A"
    email_address.short_description = 'Email Address'

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'latitude', 'longitude']
    search_fields = ['name']
    ordering = ['-id']
    list_filter = ['name']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['ride_name', 'passenger_name', 'pickup_place', 'destionation_place','status']
    search_fields = ['ride__rider__user__first_name','ride__rider__user__last_name','passenger__first_name','passenger__last_name']
    list_filter = ['status','ride__option']
    ordering = ['-id']
    list_select_related = ['ride__rider__user','passenger']

    def ride_name(self,obj):
        if obj.ride:
            return f'{obj.ride.rider.user.first_name} {obj.ride.rider.user.last_name}'
        return "N/A"
    ride_name.short_description =  'Ride Name'

    def passenger_name(self,obj):
        if obj.passenger:
            return f'{obj.passenger.first_name} {obj.passenger.last_name}'
        return "N/A"
    passenger_name.short_description =  'Passenger Name'

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']
    search_fields = ['user__first_name','user__last_name']
    ordering = ['-id']
    list_select_related = ['user']

    def user(self,obj):
        if obj.user:
            return f'{obj.user.first_name} {obj.user.last_name}'
        return "N/A"
    user.short_description =  'User Name'