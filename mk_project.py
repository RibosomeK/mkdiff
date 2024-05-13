import logging
import os
import sys

from mkdiff.fmt import RenameLog, fmt_by_dir
from mkdiff.mk_textgrid import TextGrid, save_by_config
from mkdiff.rename import recover, rename
from mkdiff.text2jyut import text2jyut

logging.getLogger().setLevel(logging.INFO)


def main():
    try:
        dir = sys.argv[1]
        if not os.path.exists(dir):
            logging.error("The directory does not exist!")
            logging.error("Try again with the correct one!")
            exit(-1)
    except IndexError:
        logging.error("Missing project directory!")
        logging.error("Try again with the directory!")
        exit(-1)

    logging.info("Now generating format configs...")
    rename_configs = fmt_by_dir(dir)
    logging.info(f"{len(rename_configs)} configs are generated.")

    logging.info("Finding existed configs...")
    existed = RenameLog.by_dir(dir)
    logging.info(f"{len(existed)} configs are found.")

    logging.info("Now saving TextGrid files...")
    for config in rename_configs:
        save_by_config(config)

    for config in existed:
        save_by_config(config)

    logging.info("Renaming...")
    for config in rename_configs:
        config.save()
        rename(config)
    for config in existed:
        rename(config)

    # logging.info("Now recovering...")
    # for config in rename_configs:
    #     recover(config)
    # for config in existed:
    #     recover(config)


if __name__ == "__main__":
    main()
