#!/usr/bin/env python3
from nltk.stem import WordNetLemmatizer

print('lemma is %s' % WordNetLemmatizer().lemmatize(input('type a word: ')))
