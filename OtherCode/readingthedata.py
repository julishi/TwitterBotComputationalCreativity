file_path = '/Users/julianashihadeh/Desktop/NoPrefaceEmilyDickinsonBooks12242.txt'
emilys_poems = open(file_path, "r")
count = 0;

#A list to hold the words read in the file. Punctuation is not sliced off of words so to keep the characteristic/style of Emily Dickinson's way of expressing ideas. 
words = [];

for line in emilys_poems:
	#the following prints each line in the text
	#print(line)
	#the following converts each line into a "list" holding the words, and prints out "empty lists" for spaces
	#print(line.split())

	#this following two lines prints every single character in a line by itself
	#for word in line:
	#	print(word)

	#the following will does two in 1 operations: 
	#1 being the line.split converts the line of text into a list
	#and 2 being, the loop traverses through all the words in the list and  prints every word with the attached grammar to it
	for word in line.split():
		#Come back to this later, for now the other data works
		if word != '-':
			if word != '--':
				for i in word:
					if i == '"':
						#print("FOUND QUOTATION")
						word = word.replace('"','')
				print(word)
				words.append(word)
				count = count + 1
		#if word.isalpha():
		#	print(word)
		#	words.append(word)
		#	count = count + 1
#print(words)
print(count)
