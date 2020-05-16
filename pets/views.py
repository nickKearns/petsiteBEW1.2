from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from pets.models import Appointment, Pet
from .forms import PetForm, AppointmentForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def home(request):
    return render(request, 'home.html')


class PetCreateView(CreateView):
    
    def get(self, request):
        context = {'form': PetForm()}
        return render(request, 'create.html', context)


    def post(self, request, *args, **kwargs):
      form = PetForm(request.POST)
      if form.is_valid():
        pet = form.save(commit=False)
        pet.owner = request.user
        pet.save()
        return HttpResponseRedirect(
            reverse('pets-list-view'))
      # else if form is not valid
      return render(request, 'create.html', { 'form': form })




class AppointmentCreateView(CreateView):
    
    def get(self, request):
        context = {'form': AppointmentForm()}
        return render(request, 'create.html', context)


    def post(self, request, *args, **kwargs):
      form = AppointmentForm(request.POST)
      if form.is_valid():
        appointment = form.save(commit=False)
        appointment.save()
        return HttpResponseRedirect(
            reverse('appointments-list-view'))
      # else if form is not valid
      return render(request, 'create.html', { 'form': form })


class AppointmentListView(ListView):

    template_name = 'appointments_list.html'
    context_object_name = 'appointments'


    def get_queryset(self):
        """Return the last five published questions."""
        return Appointment.objects.order_by('date_of_appointment')


    # def get(self, request):
    #     appointments = self.get_queryset().all()




    #     return render(request, 'appointments_list.html', {
    #         'appointments': appointments
    #     })





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



