from setuptools import setup, Extension  # type: ignore
import os
from pathlib import Path

# read the contents of README
this_directory = Path(os.path.abspath(os.path.dirname(__file__)))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

spellfix1 = Extension(
    "spellfix1",
    sources=["spellfix.c"] + (["sqlite/windows.cpp"] if os.name == 'nt' else []),
    include_dirs=[this_directory / "sqlite"] if os.name == 'nt' else []
)

setup(
    name="sqlite-spellfix",
    version="1.0.1",
    description="Loadable spellfix1 extension for sqlite",
    py_modules=["sqlite_spellfix"],
    ext_modules=[spellfix1],
    url="http://github.com/karlb/sqlite-spellfix",
    long_description=long_description,
    long_description_content_type="text/markdown",
    setup_requires=['wheel'],
)
