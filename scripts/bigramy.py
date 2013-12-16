from nltk.util import ngrams
import pandas as pd

blob = open('../data/1013.txt', 'r')
s = str(blob.read()).lower()
blob.close()

grams = ngrams(s.split(), 2)
bigramy = pd.DataFrame(data=grams)
bigramy.to_json('bigramy.json', orient='values')