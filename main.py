from mkdiff.fmt import fmt_by_dir, RenameLog
from mkdiff.rename import rename, recover
from mkdiff.lab import save_lab_by_dir
import sys

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
    dir = args[1]
    gen_rename_log(dir)
    logs = read_rename_file(dir)
    rename_file(logs)
    save_lab_by_dir(dir)


if __name__ == "__main__":
    main()
