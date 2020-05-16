from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.



class Pet(models.Model):
    pet_name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    weight_in_pounds = models.PositiveSmallIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.pet_name



    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.pet_name, allow_unicode=True)

        # Call save on the superclass.
        return super(Pet, self).save(*args, **kwargs)





class Appointment(models.Model):
    date_of_appointment = models.DateField(auto_now=True)
    duration_minutes = models.PositiveSmallIntegerField()
    special_instructions = models.CharField(max_length=256)
    pet = models.ForeignKey(Pet, on_delete=models.PROTECT)

    def __str__(self):
        return 'appointment for ' + self.pet.pet_name


    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.special_instructions, allow_unicode=True)

        # Call save on the superclass.
        return super(Appointment, self).save(*args, **kwargs)


