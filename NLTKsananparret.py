import re
import nltk
import matplotlib
from nltk import word_tokenize
from nltk.probability import FreqDist
from matplotlib import pyplot as plt
nltk.download('punkt')


import nltk.corpus  
from nltk.text import Text  
filtered = Text(nltk.corpus.gutenberg.words("/Users/milka/filtered.txt"))
filtered.concordance("sanoi")

filtered.dispersion_plot(["sanoi", "mies", "paha", "koira", "hyvä", "paha", "sika"])

filtered.generate()

