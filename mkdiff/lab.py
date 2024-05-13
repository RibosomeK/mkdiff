import os

from .fmt import RenameLog, split_copy
from .mklab import EXT, iter_wav
from .text2jyut import text2jyut


def text2lab(text: str) -> str:
    if text.encode().isalnum():
        return text
    return " ".join(text2jyut(text))


def save_lab(path: str, lab: str) -> None:
    with open(path, mode="w") as fp:
        fp.write(lab)


def save_lab_by_log(config: RenameLog):
    root = config.dir
    for root, new, original in config.iter_files():
        name, _, _ = split_copy(original)
        path = os.path.join(root, f"{os.path.splitext(new)[0]}{EXT.LAB}")
        save_lab(path, text2lab(name))


def save_lab_by_dir(dir: str):
    logs = RenameLog.by_dir(dir)
    if logs:
        for log in logs:
            save_lab_by_log(log)
    else:
        # assuming that rename function won't be used.
        for root, file in iter_wav(dir):
            name, copy, _ = split_copy(file)
            lab = text2lab(name)
            if copy == 1:
                path = os.path.join(root, f"{name}{EXT.LAB}")
            else:
                path = os.path.join(root, f"{name}{copy}{EXT.LAB}")
            save_lab(path, lab)
