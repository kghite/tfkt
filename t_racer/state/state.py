from typing import Optional
import pynecone as pc
from t_racer.models.profile import User


class State(pc.State):

    user: Optional[User] = None
