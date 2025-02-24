"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def grid() -> rx.Component:
    return rx.grid(
        rx.foreach(
            rx.Var.range(12),
            lambda i: rx.card(f"Card {i + 1}", height="10vh"),
        ),
        gap="1rem",
        grid_template_columns=[
            "1fr",
            "repeat(2, 1fr)",
            "repeat(2, 1fr)",
            "repeat(3, 1fr)",
            "repeat(4, 1fr)",
        ],
        width="100%",
    )

def index() -> rx.Component:
    return rx.container(grid())


app = rx.App()
app.add_page(index)
