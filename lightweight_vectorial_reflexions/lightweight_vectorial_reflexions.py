"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Welcome to CDIA!", font_size="4em"),
            rx.box("Bora fazer uns SVGs manêros ", rx.code(filename, font_size="1em")),
            rx.html("<h1>Bora juntos?</h1>"),
            rx.html("<svg width='100' height='100'><circle cx='50' cy='50' r='10'></svg>"),
            # what can we add?
            # rx.
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )


# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index)
app.compile()
