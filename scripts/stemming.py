#!/usr/bin/env python3
from nltk.stem.porter import PorterStemmer

print('stem is %s' % PorterStemmer().stem(input('type a word: ')))
