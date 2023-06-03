from t_racer.components import navbar
import pynecone as pc


def login():
    return pc.vstack(
        navbar(),
        pc.text("Dashboard Page"),
        spacing="1.5rem",
    )
