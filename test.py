#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 00:30:14 2022

@author: ceo
"""

from utils import *

text = "冬が来る前に、もう一度あの人とめぐり逢いたい。"


text = "亜流"
dict_ = getMecabDict(text)



# ON example
word = "水分"
target_base_pronunciation = "ふん"
target_furigana = getTargetWordFuriganaOnYomi(word,target_base_pronunciation)

print(
      "word:",word,
      "target base pronunciation:",target_base_pronunciation,
      "target actual pronunciation:",target_furigana
      )

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
word = "燃え盛る"
whole_word_pronunciation = "さかる"


target_furigana = removeOkurigana(word,whole_word_pronunciation)

print(
      "word:",word,
      "whole word pronunciation:",whole_word_pronunciation,
      "target pronunciation:",target_furigana
      )

# KUN example 3
isolated_word = "燃え盛る" 
# it works as long as the target word is the second part of the compound
# and is not inflected

whole_word_pronunciation = "さかる"
base_pronunciation = removeOkurigana(word,whole_word_pronunciation)

compound_word = "花盛り"
target_furigana = getTargetWordFuriganaKunYomi(compound_word,base_pronunciation)

print(
      "isolated_word:",word,
      "whole word pronunciation:",whole_word_pronunciation,
      "base pronunciation:",base_pronunciation,
      "compound word:", compound_word,
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
