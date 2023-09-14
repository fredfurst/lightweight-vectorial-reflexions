import reflex as rx

class LightweightvectorialreflexionsConfig(rx.Config):
    pass

config = LightweightvectorialreflexionsConfig(
    app_name="lightweight_vectorial_reflexions",
    db_url="sqlite:///reflex.db",
    telemetry_enabled=False,
    env=rx.Env.DEV,
)