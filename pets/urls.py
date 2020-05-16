from django.urls import path, include
from pets.views import AppointmentListView, PetsListView, PetDetailView, home, PetCreateView, AppointmentCreateView



urlpatterns = [
    path('', home, name='home_page'),
    path('pets/', PetsListView.as_view(), name='pets-list-view'),
    path('pets/<str:pet_name>/', PetDetailView.as_view(), name='pet-detail-view'),
    path('pets/new', PetCreateView.as_view(), name='pet-create-view'),
    path('calendar/', AppointmentListView.as_view(), name='appointments-list-view'),
    path('calendar/new', AppointmentCreateView.as_view(), name='appointment-create-view'),


]