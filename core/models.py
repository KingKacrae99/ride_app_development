from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.

class CustomUser(AbstractUser):
    Role_Choices =(
        ('Staff','Staff'),
        ('student','Student'),
        ('driver','Driver')
    )
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    profile_img = models.ImageField(default="images/user-icon.webp", upload_to='images/', null=True)
    role= models.CharField(max_length=20, choices=Role_Choices)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=['username','first_name','last_name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_slug()
        super().save(*args,**kwargs)

    def generate_slug(self):
        base_slug = slugify(f'{self.first_name}-{self.last_name}')
        unique_slug = base_slug
        number = 1

        while CustomUser.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{base_slug}-{number}'
            number += 1
        return unique_slug

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.role})'

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, related_name="staffs", on_delete=models.CASCADE)
    dept=models.CharField(max_length=100)
    post= models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.dept}'


class Student(models.Model):
    user = models.OneToOneField(CustomUser, related_name='students', on_delete=models.CASCADE)
    matric_no = models.CharField(max_length=30, unique=True)
    dept = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.dept}'

class Driver(models.Model):
    Vehicle_Choices= (
        ('bus','Bus'),
        ('tricyle','Tricycle'),
        ('bike','Bike')
    )
    STATUS_CHOICES = [
        ('available','Available'),
        ('on ride','On Ride'),
        ('unavailable','Unavailable')
    ]
    user = models.OneToOneField(CustomUser, related_name="drivers", on_delete=models.CASCADE)
    licence_no = models.CharField(max_length=50, unique=True)
    vehicle_num = models.CharField(max_length=50)
    vehicle_type = models.CharField(choices=Vehicle_Choices, max_length=20)
    vehicle_description = models.TextField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}({self.vehicle_type}) '

class Location(models.Model):
    name = models.TextField(max_length=1000)
    place_img = models.ImageField(default='images/default-map.webp', upload_to='images/', null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'

class Ride(models.Model):
    STATUS = [
       ('pending', 'Pending'),
       ('accepted', 'Accepted'),
       ('completed', 'Completed'),
       ('declined', 'Declined')
    ]
    OPTIONS = [
        ('premium','Premium'),
        ('standard','Standard')
    ]
    rider = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="riders")
    origin_place = models.ForeignKey(Location, related_name='ride_origin_places', on_delete=models.CASCADE)
    destination = models.ForeignKey(Location, related_name='ride_destination_places', on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=20, editable=False) # will be automatically assigned from the Driver.vehicle_type.
    status = models.CharField(choices=STATUS, max_length=15)
    option = models.CharField(choices=OPTIONS, max_length=15)
    available_seat = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.DateTimeField(null=True,blank=True)
    end_time = models.DateTimeField(blank = True, null=True)

    def save(self, *args, **kwargs):
        if self.rider:
            self.vehicle_type = self.rider.vehicle_type
        super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.rider.user.first_name} ({self.option} - {self.status})'

class Booking(models.Model):
    STATUS = [('booked','Booked'),('cancelled','Cancelled')]
    OPTIONS = [('premium','Premium'),('standard','Standard')]
    ride = models.ForeignKey(Ride, related_name='booking_rides', on_delete=models.CASCADE)
    passenger = models.ForeignKey(CustomUser, related_name="bookings", on_delete=models.CASCADE)
    pickup_place = models.ForeignKey(Location, related_name='booking_pickup_places', on_delete=models.CASCADE)
    destionation_place = models.ForeignKey(Location, related_name='booking_destination_places', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=15)
    ride_type = models.CharField(choices=OPTIONS, max_length=15)
    vehicle_choice = models.CharField(max_length=20)
    booked_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.ride:
            self.vehicle_choice = self.ride.vehicle_type
        super().save(*args,**kwargs)

    def __str__(self):
        return f'Booking {self.ride_type} {self.vehicle_choice}({self.status})'

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('card', 'Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('ussd', 'USSD'),
        ('wallet', 'Wallet')
    ]
    STATUS_CHOICES = [
       ('pending', 'Pending'),
       ('successful', 'Successful'),
       ('failed', 'Failed')
    ]
    ride = models.ForeignKey(Ride, related_name='ride_payments', on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomUser, related_name='payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(choices=STATUS_CHOICES,max_length=20)
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHODS)
    reference = models.CharField(max_length=30, unique=True)
    timestamp = models.DateTimeField(auto_now_add= True)

    def save(self,*args,**kwargs):
        if self.ride:
            self.amount = self.ride.price
        super().save(*args,**kwargs)


    def __str__(self):
        return f'Payment {self.id} - {self.status}'

class Wallet(models.Model):
    user = models.OneToOneField(CustomUser, related_name='wallet', on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)


