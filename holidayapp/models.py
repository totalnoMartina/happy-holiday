
from django.db import models
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField
from django_google_maps import fields as map_fields

# Models for Guest, Booking, Apartment

class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

class Guest(models.Model):
    """ Attributes of class Guest """
    guest_id = models.CharField(max_length=50, blank=False, primary_key=True)
    full_name = models.CharField(max_length=100, blank=False)
    ph_number = models.CharField(null=False, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')], max_length=40)
    email = models.EmailField(blank=False)
    kids = models.BooleanField(default=False, blank=True)
    pets = models.BooleanField(default=False, blank=True)

    def __str__(self):
        """ A method to show stored data of Guest """
        return f'A guest with an id of {self.guest_id},  {self.full_name} with a phone number: {self.ph_number} has been created!'


APARTMENTS = (('Tony', 'Tony Apartment for max4 people'),
                ('Matea', 'Matea apartment for max4 people'),
                ('Martina', 'Martina apartment for max6 people'))


class Apartment(models.Model):
    """ A class to create an apartment in offer """
    apartment_name = models.CharField(choices=APARTMENTS, max_length=10, primary_key=True)
    beds_nr = models.IntegerField()
    kitchen = models.BooleanField(default=True,name='kitchen')
    balcony = models.BooleanField(default=True, name='balcony')
    seaview = models.BooleanField(default=True, name='seaview')
    air_cond = models.BooleanField(default=True, name='AC')
    front_image = CloudinaryField('front_image', default='first_img') # cloudinary needs to store this
    front_image2 = CloudinaryField('front_image2', default='second_img') # cloudinary needs to store this
    front_image3 = CloudinaryField('front_image3', default='third_img') # cloudinary needs to store this
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    description = models.TextField(name='description', null=True)

    

    def __str__(self):
        """ Showing apartment class model created """
        return f'An apartment named {self.apartment_name} with {self.beds_nr} beds and the price of {self.price} euros is created'


