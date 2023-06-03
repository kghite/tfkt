import pynecone as pc

from datetime import datetime
from pydantic import constr
from sqlalchemy import Column, ForeignKey
from typing import Dict

from t_racer.models.mbta import Stop


class Challenge(pc.Model, table=True):
    name: constr(max_length=32)
    description: constr(max_length=256)


class ChallengeSubmission(pc.Model):
    challenge: Challenge

    started_at: datetime
    finished_at: datetime

    stops: Dict[Stop, datetime]
