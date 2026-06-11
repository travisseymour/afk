"""AFK: Keep your Mac awake by periodically moving the mouse."""

import random
import time

from pynput.mouse import Controller
import typer

app = typer.Typer(
    help="Keep your Mac awake by periodically moving the mouse a small amount.",
    no_args_is_help=False,
)

DIRECTIONS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]


def move_mouse(pixels: int = 5) -> None:
    """Move the mouse a small distance in a random direction."""
    mouse = Controller()
    dx, dy = random.choice(DIRECTIONS)
    current_x, current_y = mouse.position
    mouse.position = (current_x + dx * pixels, current_y + dy * pixels)


@app.command()
def main(
    interval: int = typer.Option(
        15,
        "--interval",
        "-i",
        help="Seconds between mouse movements.",
    ),
    pixels: int = typer.Option(
        5,
        "--pixels",
        "-p",
        help="Number of pixels to move the mouse.",
    ),
) -> None:
    """
    Periodically move the mouse to prevent the screen from sleeping.

    Press Ctrl+C to stop.
    """
    typer.echo(f"AFK running: moving mouse {pixels}px every {interval}s. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(interval)
            move_mouse(pixels)
    except KeyboardInterrupt:
        typer.echo("\nAFK stopped.")


if __name__ == "__main__":
    app()
