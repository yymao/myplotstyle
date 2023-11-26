#!/usr/bin/env python
"""
My personal plot style
Project website: https://github.com/yymao/myplotstyle
Copyright (c) 2023 Yao-Yuan Mao (yymao)
"""
import os
from setuptools import setup

_name = "myplotstyle"
_version = ""
with open(os.path.join(os.path.dirname(__file__), "{}.py".format(_name))) as _f:
    for _l in _f:
        if _l.startswith("__version__ = "):
            _version = _l.partition("=")[2].strip().strip("'").strip('"')
            break
if not _version:
    raise ValueError("__version__ not define!")

setup(
    name=_name,
    version=_version,
    description="Install my personal plot style",
    url="https://github.com/yymao/{}".format(_name),
    download_url="https://github.com/yymao/{}/archive/v{}.tar.gz".format(
        _name, _version
    ),
    author="Yao-Yuan Mao",
    author_email="yymao.astro@gmail.com",
    maintainer="Yao-Yuan Mao",
    maintainer_email="yymao.astro@gmail.com",
    license="GNU General Public License v3.0",
    license_files=('LICENSE',),
    py_modules=[_name],
    install_requires=[
        "cmasher>=1.6.0",
        "cmcrameri>=1.7.0",
    ],
)
