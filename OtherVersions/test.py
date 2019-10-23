from markovchain import JsonStorage
from markovchain.text import MarkovText, ReplyMode

markov = MarkovText()

#with open('data_extracted_6.txt') as fp:
with open('NoPrefaceEmilyDickinsonBooks12242.txt') as fp:
    markov.data(fp.read())

with open('NoPrefaceEmilyDickinsonBooks12242.txt') as fp:
    for line in fp:
        markov.data(line, part=True)
markov.data('', part=False)

print(markov())
print(markov(max_length=40, reply_to='sentence start', reply_mode=ReplyMode.END))

markov.save('markov.json')

markov = MarkovText.from_file('markov.json')


#NOTE: Fix the whole Sentence Start. Shinanigan in the output - why is it even printing that out?
