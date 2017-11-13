from numpy import array
from pickle import dump
from keras.utils import to_categorical
from keras.models import Sequential
from keras.models import Dense
from keras.layers import LSTM


#load doc into memory
def load_doc(filename):
    #open file as read only
    file = open(filename, 'r')
    #read all text
    text = file.read()
    #close the file
    file.close()
    return text

#save tokens to file
def save_doc(lines, filename):
    data = '\n'.join(lines)


def clean_text(raw_text):
    tokens = raw_text.split()
    raw_text = ' '.join(tokens)

raw_text = load_doc('rhyme.txt')
