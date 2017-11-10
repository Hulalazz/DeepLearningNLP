import nltk
from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#load data
filename = 'ALittleJourney.txt'
file = open(filename, 'rt', encoding='utf-8')
file_text = file.read()
file.close()
###########################
#some manual preprocessing#
###########################

#split into words by white space
words = file_text.split()

#convert to lower case
words = [word.lower() for word in words]

#remove punctuation from each word
table = str.maketrans('', '', punctuation)
stripped = [w.translate(table) for w in words]

#remove stop words
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]

#tokenize the list of words now converted to a string
tokens = word_tokenize(''.join(words))

#save tokenized text as new file
tokenized_file = open('ALittleJourneyTokenized.txt', 'a')
tokenized_file.write(str(tokens))
tokenized_file.close()
