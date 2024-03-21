from textgrid import TextGrid, IntervalTier
from .cantonese import PLAN_A
from enum import StrEnum
import wave

PRECISION = 5
DIFF = pow(10, -PRECISION)


class MARK(StrEnum):
    SP = "SP"
    AP = "AP"


def get_textgrid(lab_str: list[str], wav_len: float) -> TextGrid:
    """get rough textgrid str"""

    tg = TextGrid(maxTime=wav_len)
    avg_word_len = round(wav_len / (len(lab_str) + 2), PRECISION)
    word_tier = IntervalTier(name="words", minTime=0, maxTime=wav_len)
    phone_tier = IntervalTier(name="phones", minTime=0, maxTime=wav_len)

    word_tier.add(minTime=0, maxTime=avg_word_len, mark=MARK.SP)
    phone_tier.add(minTime=0, maxTime=avg_word_len, mark=MARK.SP)

    for word in lab_str:
        min_time = word_tier[-1].maxTime
        max_time = round(min_time + avg_word_len, PRECISION)
        word_tier.add(minTime=min_time, maxTime=max_time, mark=word)
        phones = PLAN_A.get_phone(word)
        avg_phone_len = round(avg_word_len / len(phones), PRECISION)
        for phone in phones:
            min_t = phone_tier[-1].maxTime
            max_t = round(min_t + avg_phone_len, PRECISION)
            phone_tier.add(minTime=min_t, maxTime=max_t, mark=phone)
        phone_tier[-1].maxTime = max_time  # align to word region
    word_tier.add(minTime=word_tier[-1].maxTime, maxTime=wav_len, mark=MARK.SP)
    phone_tier.add(minTime=phone_tier[-1].maxTime, maxTime=wav_len, mark=MARK.SP)

    tg.append(word_tier)
    tg.append(phone_tier)

    return tg


def save_textgrid(textgrid: TextGrid, path: str):
    textgrid.write(path)


def get_wav_dur(path: str) -> float:
    with wave.open(path, mode="r") as fp:
        return round(fp.getnframes() / fp.getframerate(), PRECISION)
