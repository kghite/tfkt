from .base import *

from dotenv import load_dotenv
import os

dotenv_path = os.path.join(ENVIRONMENTS['Development'])

load_dotenv(dotenv_path)
