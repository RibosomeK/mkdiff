import logging
import os
import shutil
from typing import Optional

from .fmt import RenameLog


def rename(rename_log: RenameLog):
    logging.info(f"current directory: {rename_log.dir}")
    for root, new, original in rename_log.iter_files():
        ori_path = os.path.join(root, original)
        new_path = os.path.join(root, new)
        if os.path.exists(ori_path):
            logging.info(f"new file name: {new_path}")
            logging.info(f"rename file {ori_path} to {new_path} successfully.")
            os.rename(ori_path, new_path)
        else:
            logging.warning(f"{ori_path} does not exist!")
            logging.warning("It maybe already be renamed!")


def cp_rename(rename_log: RenameLog, new_dir: str):
    logging.info(f"Current directory: {rename_log.dir}")
    logging.info(f"Now copy and rename to new directory: {new_dir}")

    if not os.path.exists(new_dir):
        logging.warning(f"Directory: {new_dir} does not exist!")
        logging.info("Now making new directory...")
        os.mkdir(new_dir)

    for root, new, original in rename_log.iter_files():
        ori_path = os.path.join(root, original)
        new_path = os.path.join(new_dir, original)

        logging.info(f"Copying {ori_path} to {new_path}")
        shutil.copyfile(ori_path, new_path)

        logging.info(f"Renaming {original} to {new}")
        os.rename(new_path, os.path.join(new_dir, new))


def recover(rename_log: RenameLog, new_dir=Optional[str]):
    if new_dir is not None:
        dir = rename_log.dir
    else:
        dir = new_dir
    logging.info(f"Current directory: {dir}")
    for _, new, original in rename_log.iter_files():
        original = os.path.join(dir, original)
        new = os.path.join(dir, new)
        if os.path.exists(new):
            logging.info(f"current file name: {new}")
            logging.info(f"recovering to file name: {original}")
            os.rename(new, original)
        else:
            logging.warning(f"{new} does not exist!")
