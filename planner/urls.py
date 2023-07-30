from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home.as_view()),
    path("gis_data", views.places_dataset, name="gis_data"),
]
