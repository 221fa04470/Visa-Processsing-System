# mainapp/models.py
from django.db import models

class PassportApplication(models.Model):
    full_name = models.CharField(max_length=255)
    dob = models.DateField()
    address = models.TextField()
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='passport_photos/')
    contact_number = models.CharField(max_length=20)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class VisaApplication(models.Model):
    full_name = models.CharField(max_length=255)
    passport_number = models.CharField(max_length=100)
    country_of_residence = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    visa_type = models.CharField(max_length=50)
    entry_type = models.CharField(max_length=50)
    travel_dates = models.DateField()
    photo = models.ImageField(upload_to='visa_photos/')
    purpose_of_visit = models.TextField()

    def __str__(self):
        return self.full_name

class ExtendedVisaApplication(models.Model):
    full_name = models.CharField(max_length=255)
    visa_number = models.CharField(max_length=100)
    reason_for_extension = models.TextField()
    requested_extension_dates = models.DateField()
    photo = models.ImageField(upload_to='extended_visa_photos/')

    def __str__(self):
        return self.full_name
