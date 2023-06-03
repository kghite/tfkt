from t_racer.components import navbar
import pynecone as pc


def manage():
    return pc.vstack(
        navbar(),
        pc.text("Manage Page"),
        spacing="1.5rem",
    )
