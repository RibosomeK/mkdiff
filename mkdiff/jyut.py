class Jyut:
    """store single char or word with jyutping(without tonal sign)"""

    _data: dict[str, tuple[str, ...]] = {}

    def __init__(self, *dict_paths: str) -> None:
        if dict_paths:
            self.append_from_files(*dict_paths)
        else:
            self.append_from_files(
                "./src/jyutping_dict/char.yaml", "./src/jyutping_dict/word.yaml"
            )

    def append_from_files(self, *dict_paths: str) -> None:
        for path in dict_paths:
            self._data.update(Jyut.load(path))

    @staticmethod
    def load(dict_path: str) -> dict[str, tuple[str, ...]]:
        data = {}
        with open(dict_path, mode="r") as fp:
            dash_stack = []
            for line in fp.readlines():
                line = line.strip()
                if line.startswith("#"):
                    continue
                if line.startswith("---"):
                    dash_stack.append("---")
                if dash_stack and not line.startswith("..."):
                    continue
                if line == "":
                    continue
                if line.startswith("..."):
                    dash_stack.pop()
                    continue
                # it's a full width comma "，"
                if b"\xef\xbc\x8c".decode("utf-8") in line:
                    continue

                try:
                    word, jyuts, _ = line.split("\t")
                except ValueError:
                    word, jyuts = line.split("\t")
                jyuts = tuple([jyut.strip("123456") for jyut in jyuts.split(" ")])
                data[word] = jyuts

            return data

    def word2jyut(self, word: str) -> tuple[str, ...]:
        """get the jyutping for a word"""
        if word in self._data:
            return self._data[word]
        else:
            jyuts = []
            for char in word:
                jyuts.extend(self._data[char])
            return tuple(jyuts)

    def __str__(self):
        return str(self._data)
