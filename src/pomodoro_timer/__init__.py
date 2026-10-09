from __future__ import annotations

import typing

from .extension import PomodoroTimer

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


def setup(api: "ExtensionsAPI") -> None:
    """Entrypoint for Biscuit to load the extension."""
    api.register("pomodoro_timer", PomodoroTimer(api))
