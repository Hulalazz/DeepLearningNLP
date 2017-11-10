import nltk
from nltk.tokenize import word_tokenize

#load data
filename = 'ALittleJourney.txt'
file = open(filename, 'rt', encoding='utf-8')
file_text = file.read()
file.close()

#some manual preprocessing
# words = file_text.split()
# tokens = word_tokenize([word.lower() for word in words])

tokens = word_tokenize(file_text)

#save tokenized text as new file
with open("ALittleJourneyTokenized.txt", "w") as output:
    output.write(str(tokens))
