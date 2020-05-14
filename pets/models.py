from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Pet(models.Model):
    pet_name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    weight_in_pounds = models.PositiveSmallIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.pet_name





class Appointment(models.Model):
    date_of_appointment = models.DateField(auto_now=True)
    duration_minutes = models.PositiveSmallIntegerField()
    special_instructions = models.CharField(max_length=256)
    pet = models.ForeignKey(Pet, on_delete=models.PROTECT)

    def __str__(self):
        return 'appointment for ' + self.pet.pet_name




