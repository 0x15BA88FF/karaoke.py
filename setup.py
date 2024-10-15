from setuptools import setup, find_packages
from pathlib import Path

NAME = "karaoke"
VERSION = "0.0.2"
DESCRIPTION = "Karaoke is a lightweight Python library designed to facilitate interactions with song Lyrics."
LONG_DESCRIPTION = (Path(__file__).parent / "README.md").read_text()

setup(
    name=NAME,
    version=VERSION,
    author="0x15BA88FF",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    keywords=["karaoke", "music", "lrc"],
    packages=find_packages(),
)