from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=255)
    phone_no1 = PhoneNumberField()
    phone_no2 = PhoneNumberField(blank=True)
    fax_no = PhoneNumberField()
    website = models.URLField(max_length=200)
    pob = models.IntegerField()
    city = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="logos/%y")

    def __str__(self):
        return self.name

