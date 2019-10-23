#Author: Juliana Shihadeh
#Computational Creativity Fall 2019
#Twitter Bot Project
#Tweets One line of Poetry
import tweepy, time, sys
import numpy as np

print("Start file")
print("Setting up URL connection")

#Setting Up Authentication to access the Twitter API
c_k = 'XqiqSs625kgEdD4Igrix2Or0l'
c_s = 'UmktY91ehm8xlmiiopfiJUkIhGwaYrbFSVTtGDumrC2d6PmJ56'
auth = tweepy.OAuthHandler(c_k, c_s)

a_k = '1185020038446641152-doTMOa9T33sd3qKlf60dg89BOSy5yN'
a_s = 'GSwT3PmV03WRpOQMV2a134WZte6fI1nJKYrF67nZWh7Ib'
auth.set_access_token(a_k, a_s)

api = tweepy.API(auth)
print(api)

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


###########################################
#THE TWEETING
###########################################
for i in range(0, 100):
	starting_word = np.random.choice(words)
	while starting_word.islower():
		starting_word = np.random.choice(words)
	
	next_word = starting_word
	poetry_line = [next_word]
	
	i = 0;
	while i < 21:
		next_word = np.random.choice(data[next_word])
		poetry_line.append(next_word)	
		i = i + 1
		
	final_string = ' '.join(poetry_line)
	api.update_status(final_string)
	#api.update_with_media('img/path', final_string)
	print(final_string)
	time.sleep(900) #tweet every 15 minutes
