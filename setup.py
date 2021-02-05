from setuptools import setup, Extension  # type: ignore

# read the contents of README
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

spellfix1 = Extension("spellfix1", sources=["spellfix.c"])

setup(
    name="sqlite-spellfix",
    version="1.0",
    description="Loadable spellfix1 extension for sqlite",
    py_modules=["sqlite_spellfix"],
    ext_modules=[spellfix1],
    url="http://github.com/karlb/sqlite-spellfix",
    long_description=long_description,
    long_description_content_type="text/markdown",
    setup_requires=['wheel'],
)
