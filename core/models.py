from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
# Create your models here.

class CustomUser(AbstractUser):
    Role_Choices =(('Staff','Staff'),
                   ('student','Student'),
                   ('driver','Driver'))
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    profile_img = models.ImageField(default="")
    slug = models.SlugField(unique=True, blank=True, editable=False)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS='username'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_slug()
        super().save(*args,**kwargs)

    def generate_slug(self):
        base_slug = slugify(f'{self.first_name.lower()}-{self.last_name.lower()}')
        unique_slug = base_slug
        number = 1

        while CustomUser.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{base_slug}-{number}'
            number += 1
        return unique_slug

    def __str__(self):
        return f'{self.first_name} ({self.last_name})'

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, related_name="staffs", on_delete=models.CASCADE)
    dept=models.CharField(max_length=100)
    post= models.CharField(max_length=100)

class Student(models.Model):
    user = models.OneToOneField(CustomUser, related_name='students', on_delete=models.CASCADE)
    matric_no = models.CharField(max_length=30, unique=True)
    dept = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)

class Driver(models.Model):
    Vehicle_Choices= (
        ('bus','Bus'),
        ('tricyle','Tricylce'),
        ('bike','Bike')
    )
    user = models.OneToOneField(CustomUser, related_name="drivers", on_delete=models.CASCADE)
    licence_no = models.CharField(max_length=50, unique=True)
    plate_num = models.CharField(max_length=20)
    vehicle_type = models.CharField(choices=Vehicle_Choices)
    vehicle_des = models.TextField(max_length=200)

class Location(models.Model):
    name = models.TextField(max_length=1000)
    place_img = models.ImageField()
    latitude = models.CharField(max_length=15, blank=True)
    longitude = models.CharField(max_length=15, blank=True)

class Ride(models.Model):
    Status = (
        ('available','Available'),
        ('on ride','On Ride'),
        ('unavailable','Unavailable')
    )
    OPTIONS = (
        ('exclusive','Exclusive'),
        ('shared','Shared')
    )
    rider = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="riders")
    origin_place = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="origin_place")
    des_place= models.ForeignKey(Location, related_name='des_place', on_delete=models.CASCADE)
    status = models.CharField(choices=Status)
    option = models.CharField(choices=OPTIONS, max_length=15)
    availabe_seat = models.IntegerField(max_length=15, default=1)
    start_time = models.DateTimeField()
    end_time = models.DateField()

class Booking(models.Model):
    STATUS = (('booked','Booked'),('cancelled',))
    OPTIONS = (('exclusive','Exclusive'),('shared','Shared'))
    Vehicle_Choices= (
        ('bus','Bus'),
        ('tricyle','Tricylce'),
        ('bike','Bike')
    )
    ride = models.ForeignKey(Ride, related_name="rides", on_delete=models.CASCADE)
    passenger = models.ForeignKey(CustomUser, related_name="customusers", on_delete=models.CASCADE)
    origin_place = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="origin_place")
    des_place= models.ForeignKey(Location, related_name='des_place', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=15)
    ride_type = models.CharField(choices=OPTIONS, max_length=15)
    vehicle_choices = models.CharField(choices=Vehicle_Choices, max_length=20)

class Payment(models.Model):
    pay_choice = (
            ('card', 'Card'),
            ('bank_transfer', 'Bank Transfer'),
            ('ussd', 'USSD'),
            ('wallet', 'Wallet')
        )
    ride = models.ForeignKey(Ride, related_name='rideS', on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomUser, related_name='customeruser', on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.CharField(choices=(('pending','Pending'), ('successful','Successful'), ('failed','Failed')),max_length=15)
    payment_method = models.CharField(max_length=30, choices=pay_choice)
    reference = models.CharField(max_length=30, unique=True)
    timestamp = models.DateField(auto_now_add= True)




