from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('places_data/', views.places_dataset, name='my_places'),
]