#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 00:30:14 2022

@author: ceo
"""

import MeCab
from suffix_trees import STree
from utils import *

# text = "冬が来る前に、もう一度あの人とめぐり逢いたい。"


# dict_ = getMecabDict(text)


word = "水分"
target_pronunciation = "ふん"

target_furigana = getTargetWordFurigana(word,target_pronunciation)