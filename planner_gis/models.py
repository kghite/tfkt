from django.contrib.gis.db import models

from challenges.models import Challenge
from users.models import Profile
from utils.file_utils import challenge_directory_path
from utils.model_utils import Named

class Stop(Named):
    location = models.PointField()
    # ID to query MBTA API for train info
    mbta_id = models.IntegerField(default=None, null=True)
    # Stored station profile (mainly for entrance / exit hints)
    station_profile = models.JSONField(default=None, null=True)

    def __str__(self):
        return f"MBTAStop(id={self.mbta_id}, name={self.name})"


class Segment(models.Model):
    nickname = models.CharField(max_length=32, default=None, null=True)

    # Segment geo
    order = models.IntegerField(default=None, null=True)
    segments = models.LineStringField()

    T = 1
    WALKING = 2
    RUNNING = 3
    TRAVEL_MODES = [
        (T, "T"),
        (WALKING, "WALKING"),
        (RUNNING, "RUNNING"),
    ]
    travel_mode = models.IntegerField(choices=TRAVEL_MODES, default=T)

    start_photo = models.ImageField(default=None, null=True, upload_to=challenge_directory_path)
    end_photo = models.ImageField(default=None, null=True, upload_to=challenge_directory_path)

    start_datetime = models.DateTimeField(default=None, null=True)
    end_datetime = models.DateTimeField(default=None, null=True)

    start_stop_id = models.IntegerField(default=None, null=True)
    end_stop_id = models.IntegerField(default=None, null=True)

    notes = models.CharField(max_length=1024, default=None, null=True)


class Route(models.Model):
    profiles = models.ManyToManyField(Profile, related_name='profiles', through='Attempt')
    segments = models.ForeignKey(Segment, on_delete=models.CASCADE)

class Attempt(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)

    start_datetime = models.DateTimeField(default=None, null=True)
    end_datetime = models.DateTimeField(default=None, null=True)
    run_notes = models.CharField(max_length=1024, default=None, null=True)
