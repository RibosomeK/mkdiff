import os

import pytest

from mkdiff.error import NoEndingNumError
from mkdiff.fmt import (RenameLog, extract_ending_num, fmt, fmt_by_dir,
                        split_copy, trim_name)


def test_split():
    assert split_copy("steam111.wav") == ("steam", 111, ".wav")
    assert split_copy("segment.wav") == ("segment", 1, ".wav")


def test_extract_ending_num():
    assert extract_ending_num("ashjkhfk12") == 12
    assert extract_ending_num("adhjqiqw23764") == 23764
    assert extract_ending_num("sff0") == 0
    assert extract_ending_num("segment1") == 1
    assert extract_ending_num("segment2") == 2
    with pytest.raises(NoEndingNumError):
        extract_ending_num("jkahdrgskjdhf")
    with pytest.raises(NoEndingNumError):
        extract_ending_num("dkfghk10k")
    with pytest.raises(NoEndingNumError):
        extract_ending_num("10dkfghkk")


def test_trim():
    assert trim_name("攔路雨偏似雪花") == "laan_lou_syut_faa"
    assert trim_name("segment") == "sent"
    assert trim_name("happy happy happy") == "hapy"
    assert trim_name("it is a happy song") == "itng"


def test_strip():
    s1 = "segment1.wav"
    name, ext = os.path.splitext(s1)
    assert name == "segment1"
    assert ext == ".wav"
    assert name.strip("0123456789") == "segment"

    s2 = "segment2.wav"
    name, ext = os.path.splitext(s2)
    assert name == "segment2"
    assert ext == ".wav"
    assert name.strip("0123456789") == "segment"


def test_fmt():
    root = "."
    files = [
        "真想不到當初我們也討厭吃苦瓜.wav",
        "用痛苦烘托歡樂 讓餘甘彰顯險惡.wav",
        "這叫半生瓜那意味著它的美年輕不會洞察嗎.wav",
        "segment1.wav",
        "segment2.wav",
        "lyrics.txt",
    ]

    assert fmt(root, files).asdict() == {
        "dir": root,
        "file_name": {
            "zan_soeng_fu_gwaa.wav": "真想不到當初我們也討厭吃苦瓜.wav",
            "jung_tung_him_ngok.wav": "用痛苦烘托歡樂 讓餘甘彰顯險惡.wav",
            "ze_giu_caat_maa.wav": "這叫半生瓜那意味著它的美年輕不會洞察嗎.wav",
            "sent.wav": "segment1.wav",
            "sent2.wav": "segment2.wav",
        },
    }


def test_fmt_dir():
    root = "./test/sample"
    result = [log.asdict() for log in fmt_by_dir(root)]
    result = sorted(result, key=lambda x: x["dir"])
    assert result == [
        {
            "dir": os.path.join(root, "song1"),
            "file_name": {
                "nei_jit_zoi_lei.wav": "你熱愛別離再合再離.wav",
                "zoi_dei_can_man.wav": "在地球上落力地親吻.wav",
                "mui_maan_go_jan.wav": "每晚大概有上億個人.wav",
            },
        },
        {
            "dir": os.path.join(root, "song2"),
            "file_name": {
                "ji_x_tau_ming.wav": "以x光眼睛把你灵魂望到很透明.wav",
                "nei_dik_git_zing.wav": "你的指甲相当洁净.wav",
                "ngo_han_si_cing.wav": "我很关注琐碎事情.wav",
            },
        },
        {
            "dir": os.path.join(root, "song3"),
            "file_name": {
                "sent.wav": "segment1.wav",
                "sent2.wav": "segment2.wav",
                "sent3.wav": "segment3.wav",
            },
        },
    ]


def test_rename_log():
    file = "./test/sample/song3/rename.json"
    assert RenameLog.from_file(file).asdict() == {
        "dir": "./test/sample/song3",
        "file_name": {
            "sent2.wav": "segment2.wav",
            "sent.wav": "segment1.wav",
            "sent3.wav": "segment3.wav",
        },
    }
