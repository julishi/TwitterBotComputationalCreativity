import random 
import sys
import numpy as np
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

###########################################
##SETTING UP LISTS TO GET DATA FROM THE DATA
#Which words are used the most, and thus which words have the most words that proceed them => these are the keys that have 
#the longest list in the dictionary
###########################################
##lengths holds the number of words that preceed every kind of word, which are the "keys" in the data dictionary
#The lengths dictionary is being created and used for sake analyzing Emily's Dickinson's words. The frequency of occurence of each word, which words she uses the most often. 
#The words she uses the most often are the words that have the largest list of words associated with the key
lengths = {}
ordered_lengths = {}
#for i in data.keys()
for i in data:
#	print("Key: {} , Value: {}".format(i,data[i]))	
	lengths[i] = len(data[i])
#	#ordered_lengths[len(data[i])] = [i]


#ALL THE KEYS AND VALUES
#lengths = sorted(lengths.values())
#for i in lengths:
#	print("Key: {}, Count Of Words After: {}".format(i,lengths[i]))	


###########################################
##THE FOLLOWING CODE IS SOURCED FROM AN ONLIINE TUTORIAL TO GET DATA ON THE DATA
#GIVES DATA ON THE FREQUENCY OF OCCURENCE OF WORDS 
########################################### 
##Getting data from the data
##SOURCE FOR BELOW CODE:https://thispointer.com/python-how-to-sort-a-dictionary-by-key-or-value/
#for key in sorted(lengths.keys()) :
#    print(key , ":" , lengths[key])

##SOURCE FOR BELOW CODE:https://thispointer.com/python-how-to-sort-a-dictionary-by-key-or-value/
# Creates a list of tuples that is listed by the value in the dictionary lengths, which is at index 1 - the value field  
#listofTuples = sorted(lengths.items() ,  key=lambda x: x[1])
 
# Iterate over the sorted sequence
#for elem in listofTuples :
#    print(elem[0] , ":" , elem[1] )

##########################################
#COMPOSING THE LINE 
##########################################
#Pick a first word, I added a feature so it picks  a capital word only but that can be taken out

starting_word = np.random.choice(words)
while starting_word.islower():
	starting_word = np.random.choice(words)
#print(starting_word)

#print(np.random.choice(data[starting_word]))
next_word = starting_word
poetry_line = [next_word]
#poetry_line.append(next_word)
#print(next_word)
i = 0;
while i < 21:
	next_word = np.random.choice(data[next_word])
	poetry_line.append(next_word)	
#	print(next_word)	
	i = i + 1

##########################################
#PRINTING THE LINE
##########################################

#####FOR PRINTING ONE LINE OF POETRY OUT ONLY USE THE FOLLOWING THREE LINES####
#print(' '.join(poetry_line))
#final_string = ' '.join(poetry_line)
#print(final_string)

######IF YOU WANT TO DIVIDE THE LINE OF POETRY INTO MULTIPLE LINES UNCOMMENT THE FOLLOWING SECTION OF CODE#########

##DIVIDE INTO LINES?
#print("The length of the poetry line list, aka how many words in the poetry line")
#print(len(poetry_line))

print("The original poetry_line list to verify the value:")
print(poetry_line)

print("Closing Word")
closing_word = np.random.choice(words)
print(closing_word)
l = len(closing_word)
print(closing_word[l-1])
c = ['.', '?', '!', ';']
while closing_word[l-1] not in c:
	closing_word = np.random.choice(words)
	print(closing_word)
	l = len(closing_word)
	
print("The chosen closing word:")
print(closing_word)

poetry_line.append(closing_word)
print("Post closing word: The original poetry_line list to verify the value:")
print(poetry_line)


#Select a hashtag word, but only select a word that has all letters in it
hashtag = np.random.choice(poetry_line)
while hashtag.isalpha() is False:
	hashtag = np.random.choice(poetry_line)
	print(hashtag)
	
print("The HashTag Word chosen is:")
hashtag = '#'+hashtag
print(hashtag)

#Select a second hashtag word, but only select a word that has all letters in it
hashtag_2 = poetry_line[len(poetry_line) - 1]
#hashtag_2 = np.random.choice(poetry_line)
#while hashtag_2.isalpha() is False:
#	hashtag_2 = np.random.choice(poetry_line)
#	print(hashtag_2)
	
	
print("The HashTag Word chosen is:")
hashtag_2 = '#'+hashtag_2


sub_list = [];
main_list = [];
if( len(poetry_line) > 5 ):
#	print("longer than 5")
	pos = 0
	while pos != len(poetry_line):
		print("pos value pre-for loop")	
		print(pos)
		for i in range(0,5):
			if(pos!=len(poetry_line)):
				print("pos: {} word: {}".format(pos, poetry_line[pos]))
				sub_list.append(poetry_line[pos])
				pos = pos + 1
		main_list.append(sub_list)
		sub_list = []


print("The entire list of lists:")
print(main_list)

print("testing join")
#final_string = ' '.join(main_list)
#print(final_string)
#
#for i in main_list:
#	print(i)
main_string = []
output = ''
for i in main_list:
	final_string = ' '.join(i)
	#print(final_string)
	output = output + '\n' + final_string
	main_string.append(final_string)

output = output + '\n' + hashtag + ' ' + hashtag_2
#for i in main_string:
#	print(i)
#print(main_string)

#a = "abc" + "\n" + "def"
#print(a)
print(output)
