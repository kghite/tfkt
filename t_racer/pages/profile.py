from t_racer.components import navbar
import pynecone as pc


def profile():
    return pc.vstack(
        navbar(),
        pc.text("Profile Page"),
        spacing="1.5rem",
    )
