import pynecone as pc

config = pc.Config(
    app_name="t_racer",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
