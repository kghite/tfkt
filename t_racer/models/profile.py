import pynecone as pc

from datetime import datetime
from pydantic import EmailStr
from pydantic import constr
from pydantic import Field
from typing import Optional


class User(pc.Model, table=True):
    email: EmailStr
    username: constr(min_length=3, regex="^[a-zA-Z0-9_-]+$")
    password: constr(min_length=7, max_length=100)

    created_at: Optional[datetime]

    is_superuser: bool = False


class ChallengeRecord(pc.Model, table=True):
    """Many-to-many through table for User/ChallengeSubmission
    """

    user: str = Field(primary_key=True)
    challenge_submission: str = Field(primary_key=True)
