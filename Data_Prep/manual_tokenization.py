import re
import string

#load the text
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

#split into words by whitespace
words = text.split()

#regex for char filtering
re_punc = re.compile('[%s]' % re.escape(string.punctuation))

#regex for non-printable char filtering
re_print = re.compile('[^%s]' % re.escape(string.printable))

#remove punctuation from each word
stripped = [re_punc.sub('', w) for w in words]

#remove nonprintable chars
result = [re_print.sub('', w) for w in stripped]

#convert to lower case
result_lower = [w.lower() for w in result]

#show result
print(result_lower[:100])
