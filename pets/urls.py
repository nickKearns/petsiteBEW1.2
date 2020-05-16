from django.urls import path, include
from pets.views import AppointmentListView, PetsListView, PetDetailView, home


urlpatterns = [
    path('', home, name='home_page'),
    path('pets/', PetsListView.as_view(), name='pets-list-view'),
    path('pets/<str:pet_id/>', PetDetailView.as_view(), name='pet-detail-view'),

]