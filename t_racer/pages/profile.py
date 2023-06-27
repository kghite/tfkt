from t_racer.components import navbar
import pynecone as pc

import folium

MAP_HEIGHT = 500

fig = folium.Figure(height=MAP_HEIGHT)
fig.add_child(folium.Map(location=[45.5236, -122.6750]))


def profile():
    return pc.vstack(
        navbar(),
        pc.text("Profile Page"),
        pc.html(fig._repr_html_().replace('"', "'"), height=MAP_HEIGHT),
        spacing="1.5rem",
    )
