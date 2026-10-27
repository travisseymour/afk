# SPDX-FileCopyrightText: AFK | Copyright (c) 2026 Travis L. Seymour, PhD <nogard@ucsc.edu>
# SPDX-License-Identifier: GPL-3.0-or-later

from datetime import datetime, timedelta
import platform
import random
import subprocess
import time
from typing import Annotated

import cyclopts
from yaspin import kbi_safe_yaspin

app = cyclopts.App(
    help="Keep your computer awake (uses caffeinate on macOS, mouse movement on Linux).",
)

IS_MACOS = platform.system() == "Darwin"

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
    """Move the mouse a small distance in a random direction (Linux only)."""
    from pynput.mouse import Controller
    mouse = Controller()
    dx, dy = random.choice(DIRECTIONS)
    current_x, current_y = mouse.position
    mouse.position = (current_x + dx * pixels, current_y + dy * pixels)


def run_caffeinate() -> None:
    """Run caffeinate -di to prevent display and idle sleep on macOS."""
    print("AFK running: using caffeinate to prevent sleep. Press Ctrl+C to stop.")
    try:
        with kbi_safe_yaspin().bold.clock as sp:
            sp.text = "Keeping system awake with caffeinate -di..."
            # caffeinate runs until interrupted
            process = subprocess.Popen(
                ["caffeinate", "-di"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            process.wait()
    except KeyboardInterrupt:
        process.terminate()
        print("\nAFK stopped.")


def run_mouse_mover(interval: int, pixels: int) -> None:
    """Run mouse mover loop for Linux."""
    print(f"AFK running: moving mouse {pixels}px every {interval}s. Press Ctrl+C to stop.")
    try:
        while True:
            with kbi_safe_yaspin().bold.clock as sp:
                next_move_time = datetime.now() + timedelta(seconds=interval)
                sp.text = f"Next mouse move at {next_move_time.strftime('%I:%M:%S %p')}..."
                time.sleep(interval)
                move_mouse(pixels)
    except KeyboardInterrupt:
        print("\nAFK stopped.")


@app.default
def main(
    *,
    interval: Annotated[int, cyclopts.Parameter(
        name=["--interval", "-i"],
        help="Seconds between mouse movements (Linux only).",
    )] = 15,
    pixels: Annotated[int, cyclopts.Parameter(
        name=["--pixels", "-p"],
        help="Number of pixels to move the mouse (Linux only).",
    )] = 5,
) -> None:
    """
    Keep your computer awake.
    On macOS: uses caffeinate (no permissions required).
    On Linux: periodically moves the mouse.
    Press Ctrl+C to stop.
    """
    if IS_MACOS:
        run_caffeinate()
    else:
        run_mouse_mover(interval, pixels)


if __name__ == "__main__":
    app()
