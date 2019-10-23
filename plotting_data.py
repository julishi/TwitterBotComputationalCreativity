import random 
import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
###########################################
#EXTRACTING THE DATA
###########################################
file_path = '/Users/julianashihadeh/Desktop/NoPrefaceEmilyDickinsonBooks12242.txt'
emilys_poems = open(file_path, "r")
count = 0;

#A list to hold the words read in the file. Punctuation is not sliced off of words so to keep the characteristic/style of Emily Dickinson's way of expressing ideas. 
words = [];

for line in emilys_poems:
	for word in line.split():
		#Come back to this later, for now the other data works
		if word != '-':
			if word != '--':
				for i in word:
					if i == '"':
						#print("FOUND QUOTATION")
						word = word.replace('"','')
				#print(word)
				words.append(word)
				count = count + 1
#print(words)
#SOURCE FOR THE DATA: http://www.gutenberg.org/ebooks/12242
print("Total words extracted from Emily Dickinson's Public Online Poems")
print(count)

###########################################
#MAKING THE DICTIONARY
###########################################
data = {}

##WRITE A DICTIONARY TO ORGANIZE ALL THE WORDS INTO KEYS (which is one word from the text) and ALL WORDS THAT PROCEED THAT WORD
#Loop through all the words and add a key for each new word that you haven't come across yet
#for i in words:
for i in range(1, len(words)):
	if data.get(words[i-1]) == None:
		#print(words[i-1])
		#print("adding a new key")
		#print("The key is:")
		#print(words[i-1])
		#print("The first value added to this key's list is:")
		#print(words[i])
		data[words[i-1]] = [words[i]]
	else:
		data[words[i-1]].append(words[i])

keys_list = data.keys()
print("Total keys in the dictionary")
print(len(keys_list))

#print(data.keys())


#%matplotlib inline
sns.set()

freqdist1 = nltk.FreqDist(words)
freqdist1.plot(100)

