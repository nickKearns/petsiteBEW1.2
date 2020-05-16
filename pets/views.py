from django.shortcuts import render
from django.views.generic import ListView, DetailView
from pets.models import Appointment, Pet
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    return render(request, 'home.html')

class AppointmentListView(ListView):
    model = Appointment

    def get(self, request):
        appointments = self.get_queryset().all()

        return render(request, 'appointments_list.html', {
            'appointments': appointments
        })





class PetsListView(ListView):
    model = Pet

    def get(self, request):


        user = self.request.user
        

        users_pets = Pet.objects.filter(owner=user)



        return render(request, 'pets_list.html', {
            'pets': users_pets
        })



class PetDetailView(DetailView):
    model = Pet

    def get(self, request, slug):

        pet = self.get_queryset().get(sluf__iexact=slug)

        return render(request, 'pet_detail.html', {
            'pet': pet,
        })



