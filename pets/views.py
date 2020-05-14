from django.shortcuts import render
from django.views.generic import ListView
from pets.models import Appointment

# Create your views here.


class AppointmentListView(ListView):
    model = Appointment

    def get(self, request):
        appointments = self.get_queryset().all()

        return render(request, 'list.html', {
            'appointments': appointments
        })