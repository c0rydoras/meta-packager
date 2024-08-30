"""jinja stuff."""

from __future__ import annotations

from jinja2 import Environment, PackageLoader

TAB = " " * 2


def array(items: list[str], newlines: bool | None = None) -> str:
    """Convert a list of strings to a bash array."""
    _newlines = (len(items) > 2) if newlines is None else newlines  # noqa: PLR2004
    brackets = [f"(\n{TAB}", "\n)"] if _newlines else "()"

    sep = f"\n{TAB}" if _newlines else " "
    return brackets[0] + sep.join([f"{i!r}" for i in items]) + brackets[1]


env = Environment(loader=PackageLoader(__package__))  # noqa: S701

env.filters["array"] = array
