import json
from typing import Optional

import pycantonese
from pycantonese.jyutping.parse_jyutping import Jyutping

from mkdiff import OpenCC


def read_lazy(file: str = "./src/dictionary/lazy.json") -> dict[str, str]:
    with open(file, mode="r") as fp:
        return json.load(fp)


def to_no_tone(jyut: Jyutping) -> str:
    return jyut.onset + jyut.nucleus + jyut.coda


def text2jyut(text: str, lazy: Optional[dict[str, str]] = read_lazy()) -> list[str]:
    """convert text into jyutping, numbers will also be converted"""
    if lazy is None:
        lazy = {}

    jyuts: list[str] = []
    text = OpenCC.convert(text)

    for key, val in lazy.items():
        text = text.replace(key, val)

    # if text only contain letter number and space
    if all(char.encode().isalnum() or char.encode().isspace() for char in text):
        return text.split(" ")

    for word, jyut in pycantonese.characters_to_jyutping(text):
        if jyut is None and word.isalpha():
            jyuts.append(word)
        else:
            for jp in pycantonese.parse_jyutping(jyut):
                jyuts.append(lazy.get(to_no_tone(jp), to_no_tone(jp)))
    return jyuts
