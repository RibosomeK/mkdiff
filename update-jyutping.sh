#!/bin/bash
JYUTPING_DIR="./src/jyutping_dict"

CHAR_URL="https://raw.githubusercontent.com/rime/rime-cantonese/main/jyut6ping3.chars.dict.yaml"
WORD_URL="https://raw.githubusercontent.com/rime/rime-cantonese/main/jyut6ping3.words.dict.yaml"
PHRASE_URL="https://raw.githubusercontent.com/rime/rime-cantonese/main/jyut6ping3.phrase.dict.yaml"

CHAR="${JYUTPING_DIR}/char.yaml"
WORD="${JYUTPING_DIR}/word.yaml"
PHRASE="${JYUTPING_DIR}/phrase.yaml"

wget "$CHAR_URL" -O "$CHAR"
wget "$WORD_URL" -O "$WORD"
wget "$PHRASE_URL" -O "$PHRASE"
