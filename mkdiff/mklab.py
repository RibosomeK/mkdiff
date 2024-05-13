import os
from enum import StrEnum
from typing import Iterator


class EXT(StrEnum):
    WAV = ".wav"
    JSON = ".json"
    LAB = ".lab"
    TextGrid = ".TextGrid"


def iter_wav(dir: str) -> Iterator[tuple[str, str]]:
    """yield (root, file_name)"""
    for root, _, files in os.walk(dir):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext == EXT.WAV:
                yield root, file
