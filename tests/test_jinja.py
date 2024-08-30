from __future__ import annotations

import pytest

from meta_packager.jinja import array


@pytest.mark.parametrize(
    ("input", "expected", "newlines"),
    [
        (["foo"], "('foo')", None),
        (["foo", "bar"], "('foo' 'bar')", None),
        (
            ["foo: for testing", "bar: for testing"],
            "(\n  'foo: for testing'\n  'bar: for testing'\n)",
            True,
        ),
        (
            ["foo: for testing", "bar: for testing", "baz: for testing"],
            "(\n  'foo: for testing'\n  'bar: for testing'\n  'baz: for testing'\n)",
            None,
        ),
        (
            ["foo: for testing", "bar: for testing", "baz: for testing"],
            "('foo: for testing' 'bar: for testing' 'baz: for testing')",
            False,
        ),
    ],
)
def test_array(items: list[str], expected: str, newlines: bool | None) -> None:
    assert array(items, newlines) == expected
