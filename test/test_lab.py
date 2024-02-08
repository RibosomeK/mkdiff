from mkdiff.lab import text2lab


def test_lab():
    assert text2lab("做人沒有苦澀可以嗎") == "zou jan mut jau fu gip ho ji maa"
    assert text2lab("做人没有苦涩可以吗？") == "zou jan mut jau fu gip ho ji maa"
    assert text2lab("至共你覺得苦也不太差") == "zi gung nei gok dak fu jaa bat taai caa"
    assert text2lab("至共你觉得苦也，不太差") == "zi gung nei gok dak fu jaa bat taai caa"
