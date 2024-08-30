#!/usr/bin/env python3

"""Draft main."""

from pathlib import Path

import tomllib

from meta_packager.jinja import env

template = env.get_template("PKGBUILD.j2")

with Path("packages.toml").open("rb") as f:
    data = tomllib.load(f)

for _package in data["package"]:
    pass
