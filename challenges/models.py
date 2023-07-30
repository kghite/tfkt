from django.contrib.gis.db import models

from utils.file_utils import challenge_directory_path
from utils.model_utils import Named


class Challenge(Named):
    rules = models.JSONField(default=None, null=True)
    start_date = models.DateField(default=None, null=True)
    end_date = models.DateField(default=None, null=True)

    cover_photo = models.ImageField(
        default=None, null=True, upload_to=challenge_directory_path
    )

    def __str__(self):
        return self.name
