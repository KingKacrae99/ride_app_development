from django.contrib import admin
from core.models import *

# Register your models here..
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
    email_address.short_description = 'Email_Address'