#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 00:30:14 2022

@author: ceo
"""

from utils import *

import MeCab
tagger = MeCab.Tagger()

text = "冬が来る前に、もう一度あの人とめぐり逢いたい。"


text = "積乱雲"
dict_ = getMecabDict(text)
parsing = tagger.parse(text).split("	")
# print(parsing)

text = "さんご礁"
dict_ = getMecabSimpleParserDict(text)

# text = "積乱雲"
# dict_ = getMecabSimpleParserDict(text)



# ON example
word = "水分"
target_base_pronunciation = "ふん"
target_furigana = getTargetWordFurigana(word,target_base_pronunciation)

print(
      "word:",word,
      "target base pronunciation:",target_base_pronunciation,
      "target actual pronunciation:",target_furigana
      )


# ON example2
word = "さんご礁"
target_base_pronunciation = "しょう"
target_furigana = getTargetWordFurigana(word,target_base_pronunciation)

print(
      "word:",word,
      "target base pronunciation:",target_base_pronunciation,
      "target actual pronunciation:",target_furigana
      )

STOP
# KUN example 1
word = "獲る"
whole_word_pronunciation = "える"

target_furigana = removeOkurigana(word,whole_word_pronunciation)

print(
      "word:",word,
      "whole word pronunciation:",whole_word_pronunciation,
      "target pronunciation:",target_furigana
      )


# KUN example 2
word = "盛る"
whole_word_pronunciation = "さかる"


target_furigana = removeOkurigana(word,whole_word_pronunciation)

print(
      "word:",word,
      "whole word pronunciation:",whole_word_pronunciation,
      "target pronunciation:",target_furigana
      )

# KUN example 3
kanji = "盛"
word = "燃え盛る" 
isolated_word_pronunciation = "さかる"
base_pronunciation = getBasePronunciationKunYomi(kanji,word,isolated_word_pronunciation)

word = "花盛り"
target_furigana = getTargetWordFurigana(word,base_pronunciation)

print(
      "isolated_word:",word,
      "whole word pronunciation:",whole_word_pronunciation,
      "base pronunciation:",base_pronunciation,
      "compound word:", word,
      "target pronunciation:", target_furigana
      )

# KUN example 4
word = "占う"
whole_word_pronunciation = "うらなう"

target_furigana = removeOkurigana(word,whole_word_pronunciation)

print(
      "word:",word,
      "whole word pronunciation:",whole_word_pronunciation,
      "target pronunciation:",target_furigana
      )


# KUN example 5
kanji = "橋"
word = "丸木橋" 
isolated_word_pronunciation = "はし"
base_pronunciation = getBasePronunciationKunYomi(kanji,word,isolated_word_pronunciation)
target_furigana = getTargetWordFurigana(word,base_pronunciation)

print(
      "word:",word,
      "whole word pronunciation:",whole_word_pronunciation,
      "target pronunciation:",target_furigana
      )


#########################

# kanji = "汚"
# example = "汚す"
# whole_word_furigana = "けがす"

# base_pronunciation = getBasePronunciationKunYomi(kanji,example,whole_word_furigana)
# getTargetWordFurigana(example,base_pronunciation)


