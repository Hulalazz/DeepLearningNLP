from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

#load data
filename = 'MasqueofRedDeath.txt'
file = open(filename, 'rt', encoding=None)
file_text = file.read()
file.close()

###
## Text Cleaning
#

#split words by white space and convert to lower case
words = file_text.split()
words = [word.lower() for word in words]
print(words)

#train model
model = Word2Vec(words, min_count=5)

#fit 2D PCA model to vectors
X = model[model.wv.vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)

#create scatter plot of the projection
pyplot.scatter(result[:,0], result[:, 1])
words = list(model.wv.vocab)

for i, word in enumerate(words):
    pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()
