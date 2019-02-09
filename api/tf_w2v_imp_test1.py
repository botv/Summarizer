import numpy as numpy
import tensorflow as tensorflow

corpus_raw = 'He is the king . The king is royal . She is the royal  queen '

corpus_raw = corpus_raw.lower()

words = []

for word in corpus_raw.split():
	if word != '.':
		words.append(word)

words = set(words)
