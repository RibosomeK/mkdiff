import logging
import os

from .fmt import RenameLog


def rename(rename_log: RenameLog):
    logging.info(f"current directory: {rename_log.dir}")
    for root, new, original in rename_log.iter_files():
        original = os.path.join(root, original)
        new = os.path.join(root, new)
        if os.path.exists(original):
            logging.info(f"new file name: {new}")
            logging.info(f"rename file {original} to {new} successfully.")
            os.rename(original, new)
        else:
            logging.warning(f"{original} does not exist!")


def recover(rename_log: RenameLog):
    logging.info(f"current directory: {rename_log.dir}")
    for root, new, original in rename_log.iter_files():
        original = os.path.join(root, original)
        new = os.path.join(root, new)
        if os.path.exists(new):
            logging.info(f"current file name: {new}")
            logging.info(f"recovering to file name: {original}")
            os.rename(new, original)
        else:
            logging.warning(f"{new} does not exist!")
