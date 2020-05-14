from django.urls import path, include
from pets.views import AppointmentListView


urlpatterns = [
    path('', AppointmentListView.as_view(), name='appointment-list-view')
]