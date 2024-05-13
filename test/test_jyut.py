from mkdiff import JYUT
from mkdiff.text2jyut import text2jyut


def test_jyut():
    assert JYUT.word2jyut("你好") == ("nei", "hou")
    assert JYUT.word2jyut("我我") == ("ngo", "ngo")


def test2jyut():
    assert text2jyut("我我") == ["ngo", "ngo"]
    assert text2jyut("險惡") == ["him", "ngok"]
    assert text2jyut("做人沒有苦澀可以嗎") == "zou jan mut jau fu gip ho ji maa".split(
        " "
    )
    assert text2jyut("討厭eat苦瓜") == ["tou", "jim", "eat", "fu", "gwaa"]
    assert text2jyut("討厭 eat 苦瓜") == ["tou", "jim", "eat", "fu", "gwaa"]
    assert text2jyut("nei zoi but nung ze") == "nei zoi but nung ze".split(" ")
