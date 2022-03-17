#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 12:04:55 2022

@author: milka
"""
import re
import nltk
import matplotlib
from nltk import word_tokenize
from nltk.probability import FreqDist
from matplotlib import pyplot as plt
nltk.download('punkt')


with open(file = "/Users/milka/SananparsiData.csv") as f:
    text = f.read()
    
print(text)

pipeline = [('""', ' '),('"""', ' '), ('"', ' ')]

for old, new in pipeline:
    text = text.replace(old, new)
    print(text)
    
stops = re.compile(r"\d")
text = stops.sub(repl="", string=text)
print(text)

punct = re.compile(r'(\.|,){1,}')
text = punct.sub(repl="", string=text)
print(text)

text = text.lower()
wordlist = text.split()
print(wordlist)

def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

words = word_tokenize(text)


from nltk.corpus import stopwords
filtered_words = [word for word in wordlist if word not in stopwords.words('finnish')]
new_stopwords = ['kyllä', 'ei', 'eikä']
filtered_words.extend(new_stopwords)


fdist = FreqDist(filtered_words)
fdist.most_common(20)
fdist.plot(20)
plt.show()

with open('filtered.txt', 'w') as f:
    f.write(str(filtered_words))

