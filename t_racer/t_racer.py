"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc

from t_racer.pages import dashboard, login, profile, manage
from t_racer.state import State

app = pc.App(state=State)
app.add_page(login)
app.add_page(profile)
app.add_page(manage)
app.add_page(dashboard, route="/")
app.compile()
