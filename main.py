import logging
import os
import sys

from mkdiff.fmt import RenameLog, fmt_by_dir
from mkdiff.lab import save_lab_by_dir
from mkdiff.mk_textgrid import get_textgrid, get_wav_dur
from mkdiff.rename import recover, rename

TEST_DIR = "./test/sample"


def gen_rename_log(dir: str):
    rename_log = fmt_by_dir(dir)
    for log in rename_log:
        log.save()


def read_rename_file(dir: str) -> list[RenameLog]:
    return RenameLog.by_dir(dir)


def rename_file(rename_logs: list[RenameLog]):
    for log in rename_logs:
        rename(log)


def recover_file(rename_logs: list[RenameLog]):
    for log in rename_logs:
        recover(log)


args = sys.argv


def main():
    try:
        dir = args[1]
        if not os.path.exists(dir):
            logging.error("The directory does not exist!")
            logging.error("Try again with the correct one!")
            return
    except IndexError:
        logging.error("Missing project directory!")
        logging.error("Try again with the directory!")
        return

    # dir = args[1]
    # gen_rename_log(dir)
    # logs = read_rename_file(dir)
    # rename_file(logs)
    # save_lab_by_dir(dir)

    # wav = "./test/sample/textgrid/zan_soeng_fu_gwaa.wav"
    # dur = get_wav_dur(wav)
    # get_textgrid(
    #     [
    #         "zan",
    #         "soeng",
    #         "bat",
    #         "dou",
    #         "dong",
    #         "co",
    #         "ngo",
    #         "mun",
    #         "jaa",
    #         "tou",
    #         "jim",
    #         "hek",
    #         "fu",
    #         "gwaa",
    #     ],
    #     dur,
    # ).write(os.path.splitext(wav)[0] + ".TextGrid")


if __name__ == "__main__":
    main()
