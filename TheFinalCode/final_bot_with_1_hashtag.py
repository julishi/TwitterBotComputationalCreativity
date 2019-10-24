#Author: Juliana Shihadeh
#Computational Creativity Fall 2019
#Twitter Bot Project
#Tweets multiple lines of poetry with 2 hashtags
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
##For anyone else using this code, insert Path of the Text File Wherever it's donwloaded on the computer the code is being run on
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
		data[words[i-1]] = [words[i]]
	else:
		data[words[i-1]].append(words[i])

keys_list = data.keys()
print("Total keys in the dictionary")
print(len(keys_list))

###########################################
#PREPARING THE TWEET TEXT
###########################################
for i in range(0, 100):

##Select a starting word
	starting_word = np.random.choice(words)
	while starting_word.islower():
		starting_word = np.random.choice(words)

##Add the body text of the poem
	next_word = starting_word
	poetry_line = [next_word]

	i = 0;
	while i < 21:
		next_word = np.random.choice(data[next_word])
		poetry_line.append(next_word)	
		i = i + 1
		
##Add the closing word of the poetry line

	closing_word = np.random.choice(words)
	l = len(closing_word)
	c = ['.', '?', '!', ';']
	while closing_word[l-1] not in c:
		closing_word = np.random.choice(words)
		l = len(closing_word)
		
	poetry_line.append(closing_word)

##Prepare a hashtag for the poem by selecting one of the words in the poem that was created,
##but append it at the end after the poem is syntaxed as needed to add it as a new line attached to the poem
##Only select a word that has all letters in it
	hashtag = np.random.choice(poetry_line)	
	while hashtag.isalpha() is False:
		hashtag = np.random.choice(poetry_line)
		
	hashtag = '#'+hashtag

##Convert the list of words in the poetry_line into 1 String Variable with Multiple Lines 
	sub_list = [];
	main_list = [];
	pos = 0
	while pos != len(poetry_line):
		for i in range(0,5):
			if(pos!=len(poetry_line)):
				sub_list.append(poetry_line[pos])
				pos = pos + 1
		main_list.append(sub_list)
		sub_list = []

	main_string = []
	output = ''
	for i in main_list:
		final_string = ' '.join(i)
		output = output + '\n' + final_string
		main_string.append(final_string)

##Add the hashtag onto the poem
	tweet = output + '\n' + hashtag
##And print out the final tweet in the console/terminal
	print(tweet)

###########################################
#TWEETING THE POEM TO TWITTER
###########################################
	api.update_status(tweet)
##Line of code for adding an image with the tweet if wanted
	#api.update_with_media('img/path', tweet)
	time.sleep(15) #Change time as needed 
