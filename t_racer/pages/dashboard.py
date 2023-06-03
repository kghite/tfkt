from t_racer.components import navbar
import pynecone as pc


def dashboard():
    return pc.vstack(
        navbar(),
        pc.text("Dashboard Page"),
        spacing="1.5rem",
    )
