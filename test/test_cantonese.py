from mkdiff.cantonese import PLAN_A
import pytest


def test_plan_a():
    assert PLAN_A.get_phone("ngo") == ("ng", "oh")
    assert PLAN_A.get_phone("ngau") == ("ng", "ax", ":u")
    assert PLAN_A.get_phone("jaa") == ("y", "aa")
    assert PLAN_A.get_phone("ang") == ("ax", ":g")
    assert PLAN_A.get_phone("m") == ("m",)
    assert PLAN_A.get_phone("ng") == ("ng",)
    with pytest.raises(KeyError):
        PLAN_A.get_phone("juan")
