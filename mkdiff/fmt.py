import json
import logging
import os
from dataclasses import asdict, dataclass, field
from typing import Any, Callable, Iterable, Iterator, Self

from .error import NoEndingNumError
from .mklab import EXT
from .text2jyut import text2jyut

RENAME = "rename.json"

"""
json format be like:
{
    "dir": "the/directory",
    "file_name": {
        "new_file_name": "original_file_name",
        ...
    }
}
"""


@dataclass
class RenameLog:
    dir: str = "."
    file_name: dict[str, str] = field(default_factory=dict)

    def asdict(self) -> dict[str, Any]:
        return asdict(self)

    def iter_files(self) -> Iterator[tuple[str, str, str]]:
        """return root new file and original"""
        root = self.dir
        for new, original in self.file_name.items():
            yield root, new, original

    def save(self):
        logging.info("Saving config...")
        logging.info(f"Current directory: {self.dir}")
        with open(os.path.join(self.dir, RENAME), mode="w") as fp:
            json.dump(self.asdict(), fp, ensure_ascii=False, indent=2)
            logging.info("Saved successfully")

    @classmethod
    def from_file(cls, file: str) -> Self:
        if os.path.exists(file):
            with open(file, mode="r") as fp:
                return cls(**json.load(fp))
        else:
            raise FileNotFoundError(f"{file} does not exist!")

    @classmethod
    def by_dir(cls, dir: str) -> list[Self]:
        rename_logs: list[Self] = []
        for root, _, files in os.walk(dir):
            for file in files:
                if file == RENAME:
                    rename_logs.append(cls.from_file(os.path.join(root, file)))
        return rename_logs


def extract_ending_num(s: str) -> int:
    num: list[int] = []
    for i in range(len(s)):
        try:
            num.append(int(s[-(i + 1)]))
        except ValueError:
            break
    if not num:
        raise NoEndingNumError(f"String: {s} does not end with number.")
    number = 0
    for i, n in enumerate(num):
        number += pow(10, i) * n
    return number


def split_copy(file: str) -> tuple[str, int, str]:
    """return (name, copy, ext)"""
    name, ext = os.path.splitext(file)
    try:
        copy = extract_ending_num(name)
        name = name[: -len(str(copy))]
    except NoEndingNumError:
        copy = 1
    return name, copy, ext


def _trim(name: str, to_jyut: Callable[[str], Iterable[str]] = text2jyut) -> str:
    """take two chars at the beginning and the end to form new name"""
    new_name = name[:2] + name[-2:]
    return "_".join(to_jyut(new_name))


def trim_name(name: str, rule: Callable[[str], str] = _trim) -> str:
    return rule(name)


def fmt(
    root: str, files: list[str], rule: Callable[[str], str] = trim_name
) -> RenameLog:
    rename_log: RenameLog = RenameLog(dir=root)
    file_name = rename_log.file_name
    for file in files:
        name, copy, ext = split_copy(file)
        if ext == EXT.WAV:
            new_name = rule(name)
            if copy == 1:
                new_file = f"{new_name}{ext}"
            else:
                new_file = f"{new_name}{copy}{ext}"
            while new_file in file_name:
                copy += 1
                new_file = f"{new_name}{copy}{ext}"
            file_name[new_file] = file
    return rename_log


# def _fmt(file: str, rule: Callable[[str], str] = trim_name) -> tuple[str, int, str]:
#     """return (file_name, copy, .wav)"""
#     name, copy, ext = split_copy(file)
#     if ext != EXT.WAV:
#         raise TypeError(f"Wron file type: {file}")
#     return rule(name), copy, EXT.WAV


def fmt_by_dir(dir: str, rule: Callable[[str], str] = trim_name) -> list[RenameLog]:
    """walk through directory including sub folders.
    formatting file names, log in a json file."""

    if not os.path.exists(dir):
        raise FileNotFoundError

    rename_log: list[RenameLog] = []

    # log = RenameLog()
    # for root, file in iter_wav(dir):
    #     if log.dir != root:
    #         if log.file_name:
    #             rename_log.append(log)
    #     else:
    #         log = RenameLog(root)
    #         name, copy, ext = _fmt(file, rule)
    #         if copy == 1:
    #             new_file = f"{name}{ext}"
    #         else:
    #             new_file = f"{name}{copy}{ext}"
    #         while new_file in log.file_name:
    #             copy += 1
    #             new_file = f"{name}{copy}{ext}"
    #         log.file_name[new_file] = file

    for root, _, files in os.walk(dir):
        if os.path.exists(os.path.join(root, RENAME)):
            logging.info(f"Directory {root} already contain a rename.json.")
            logging.info("Skipping...")
            continue
        if files:
            rename_log.append(fmt(root, files, rule))

    return rename_log
