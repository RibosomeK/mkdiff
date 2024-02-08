import logging

WORD = (
    "aa aai aak aam aan aang aap aat aau "
    "ai ak am ang ap au "
    "baa baai baak baan baang baau "
    "bai bak bam ban bang bat bau "
    "be bei bek beng "
    "bik bin bing bit biu "
    "bo bok bong bou "
    "bui buk bun bung but "
    "caa caai caam caan caang caap caat caau "
    "cai cak cam can cang cap cat cau "
    "ce cek ceng ceoi ceon ceot "
    "ci cik cim cin cing cip cit ciu "
    "co coek coeng coi cok cong cou "
    "cuk cun cung "
    "cyu cyun cyut "
    "daa daai daak daam daan daap daat "
    "dai dak dang dap dat dau "
    "de dei dek deng deoi deon deot deu "
    "di dik dim din ding dip dit diu "
    "do doe doek doi dok dong dou "
    "duk dung dyun dyut "
    "e ei "
    "faa faai faak faan faat "
    "fai fan fang fat fau "
    "fe fei "
    "fiu "
    "fo fok fong "
    "fu fui fuk fun fung fut "
    "gaa gaai gaak gaam gaan gaang gaap gaat gaau "
    "gai gam gan gang gap gat gau "
    "ge gei geng geoi gep "
    "gik gim gin ging gip git giu "
    "go goe goek goeng goi gok gon gong got gou "
    "gu gui guk gun gung "
    "gwaa gwaai gwaak gwaan gwaang gwaat "
    "gwai gwan gwang gwat "
    "gwik gwing "
    "gwo gwok gwong "
    "gyun gyut "
    "haa haai haak haam haan haang haap haau "
    "hai hak ham han hang hap hat hau "
    "hei hek heng heoi "
    "hik him hin hing hip hit hiu "
    "ho hoe hoeng hoi hok hon hong hot hou "
    "huk hung hyun hyut "
    "jaa jaai jaak jai jam jan jap jat jau "
    "je jeng jeoi jeon "
    "ji jik jim jin jing jip jit jiu "
    "jo joek joeng jou "
    "juk jung jyu jyun jyut "
    "kaa kaai kaat kaau "
    "kai kam kan kang kap kat kau "
    "ke kei kek keoi "
    "kik kim kin king kit kiu "
    "ko koe koek koeng koi kok kong "
    "ku kui kuk kung kut "
    "kwaa kwaai kwaang kwai kwan "
    "kwik kwok kwong "
    "kyun kyut "
    "laa laai laak laam laan laang laap laat laau "
    "lai lak lam lang lap lat lau "
    "le lei lek lem leng leoi leon leot "
    "li lik lim lin ling lip lit liu "
    "lo loek loeng loi lok long lou "
    "luk lung lyun lyut "
    "m maai maak maan maang maat maau "
    "mai mak mam man mang mat mau "
    "me mei meng "
    "mi mik min ming mit miu "
    "mo mok mong mou "
    "mui muk mun mung mut "
    "naa naai naam naan naap naat naau "
    "nai nak nam nan nang nap nat nau "
    "ne nei neoi neot "
    "ng ngaa ngaai ngaak ngaam ngaan ngaang ngaap ngaat ngaau "
    "ngai ngak ngam ngan ngang ngap ngat ngau "
    "ngit ngo ngoi ngok ngon ngong ngou nguk ngung "
    "ni nik nim nin ning nip niu "
    "no noeng noi nok nong nou "
    "nuk nung nyun "
    "o oi ok on ong ou "
    "paa paai paak paan paang paat paau "
    "pai pan pang pat pau "
    "pei pek peng "
    "pik pin ping pit piu "
    "po poi pok pong pou "
    "pui puk pun pung put "
    "saa saai saak saam saan saang saap saat saau "
    "sai sak sam san sang sap sat sau "
    "se sei sek seng seoi seon seot "
    "si sik sim sin sing sip sit siu "
    "so soek soeng soi sok song sou "
    "suk sung syu syun syut "
    "taa taai taam taan taap taat "
    "tai tam tan tang tau "
    "tek teng teoi teon "
    "tik tim tin ting tip tit tiu "
    "to toe toi tok tong tou "
    "tuk tung tyun tyut "
    "uk ung "
    "waa waai waak waan waang waat "
    "wai wan wang wat "
    "wik wing "
    "wo wok wong wu wui wun wut "
    "zaa zaai zaak zaam zaan zaang zaap zaat zaau "
    "zai zak zam zan zang zap zat zau "
    "ze zek zeng zeoi zeon zeot "
    "zi zik zim zin zing zip zit ziu "
    "zo zoek zoeng zoi zok zong zou "
    "zuk zung zyu zyun zyut"
).split(" ")


VOWEL = set(
    (
        "aa aai aau aan aam aang "
        "aat aak aap "
        "ai au an am ang "
        "at ak ap "
        "i iu in im ing "
        "it ik ip "
        "u ui un ung "
        "ut uk "
        "e ei eu em eng "
        "ek ep "
        "o oi ou on ong "
        "ok "
        "oe oeng "
        "eoi eon eot "
        "yu yun yut "
        "m n ng"
    ).split(" ")
)

CONSONANT = set("b c d f g gw h j k kw l m n ng p s t w z".split(" "))


class PLAN_A:
    VOWEL: dict[str, tuple[str, ...]] = {
        "aa": ("aa",),
        "aai": ("aa", ":i"),
        "aau": ("ah", ":u"),
        "aan": ("aa", ":n"),
        "aam": ("aa", ":m"),
        "aang": ("ah", ":g"),
        "aat": ("aa", ":t"),
        "aak": ("aa", ":k"),
        "aap": ("aa", ":p"),
        "ai": ("ax", ":i"),
        "au": ("ax", ":u"),
        "an": ("ax", ":n"),
        "am": ("ax", ":m"),
        "ang": ("ax", ":g"),
        "at": ("ax", ":t"),
        "ak": ("ax", ":k"),
        "ap": ("ax", ":p"),
        "i": ("iy",),
        "iu": ("iy", ":u"),
        "in": ("iy", ":n"),
        "im": ("iy", ":m"),
        "ing": ("ih", ":g"),
        "it": ("iy", ":t"),
        "ik": ("ih", ":k"),
        "ip": ("iy", ":p"),
        "u": ("uw",),
        "ui": ("uw", ":i"),
        "un": ("uw", ":n"),
        "ung": ("ox", ":g"),
        "ut": ("uw", ":t"),
        "uk": ("ox", ":k"),
        "e": ("eh",),
        "ei": ("ih", ":i"),
        "eu": ("ea", ":u"),
        "em": ("ea", ":m"),
        "eng": ("ea", ":g"),
        "ek": ("ea", ":k"),
        "ep": ("ea", ":p"),
        "o": ("oh",),
        "oi": ("oh", ":i"),
        "ou": ("ox", ":u"),
        "on": ("oh", ":n"),
        "ong": ("oh", ":g"),
        "ot": ("oh", ":t"),
        "ok": ("oh", ":k"),
        "oe": ("oe",),
        "oeng": ("oe", ":g"),
        "oek": ("oe", ":k"),
        "eoi": ("eo", ":i"),
        "eon": ("eo", ":n"),
        "eot": ("eo", ":t"),
        "yu": ("vw",),
        "yun": ("vw", ":n"),
        "yut": ("vw", ":t"),
        "m": ("m",),
        "n": ("n",),
        "ng": ("ng",),
    }
    CONSONANT: dict[str, tuple[str, ...]] = {
        "gw": ("g", "w"),
        "kw": ("k", "w"),
        "j": ("y",),
    }


def get_plan_a() -> list[tuple[str, ...]]:
    scheme: list[tuple[str, ...]] = []
    for word in WORD:
        if word in VOWEL:
            scheme.append((word, *PLAN_A.VOWEL[word]))
        elif word in CONSONANT:
            scheme.append((word, *PLAN_A.CONSONANT[word]))
        else:
            for c in CONSONANT:
                if word.startswith(c) and (v := word[len(c) :]) in PLAN_A.VOWEL:
                    scheme.append((word, *PLAN_A.CONSONANT.get(c, c), *PLAN_A.VOWEL[v]))
                    break
            else:
                logging.warning(f"Unknown word: {word}")
    return scheme


def save_scheme(scheme: list[tuple[str, ...]], path: str):
    with open(path, mode="w") as fp:
        for line in scheme:
            fp.write(f"{line[0]}\t{" ".join(line[1:])}\n")


if __name__ == "__main__":
    save_scheme(get_plan_a(), "./src/dictionary/cantonese-opencpop.txt")
