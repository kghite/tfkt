import os

from dotenv import load_dotenv

from .base import *

dotenv_path = os.path.join(ENVIRONMENTS["Development"])

load_dotenv(dotenv_path)
