from django.contrib.gis.db.models.functions import \
    Distance  # distance between us and fav places
from django.contrib.gis.geos import (  # to get our longitude and latitude
    Point, fromstr)
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views import generic  # django generic view

from .models import Stop

longitude = -80.191788
latitude = 25.761681
my_location = Point(longitude, latitude, srid=4326)


class Home(generic.ListView):
    model = Stop
    context_object_name = "places"
    queryset = Stop.objects.annotate(
        distance=Distance("location", my_location)
    ).order_by("distance")[0:6]
    template_name = "home.html"


def places_dataset(request):
    place = serialize("geojson", Stop.objects.all())

    return HttpResponse(place, content_type="json")
