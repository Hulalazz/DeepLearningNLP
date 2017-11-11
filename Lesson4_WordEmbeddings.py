from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

#define training data
sentences = [['this', 'is', 'my', 'first', 'sentence', 'for', 'this', 'test', 'on', 'word2vec'],
['this', 'is', 'the', 'second', 'sentence'],
['all', 'comedy', 'comes', 'in', 'threes'],
['i', 'am', 'all', 'four', 'female', 'politicians', 'and', 'all', 'that', 'jazz'],
['and', 'the', 'deed', 'was', 'done', 'i', 'had', 'gotten', 'to', 'five']]

#train model
model = Word2Vec(sentences, min_count=1) #Word2Vec(vocab=31, size=100, alpha=0.025)

#fit 2D Principal Component for Analysis model to vectors
X = model[model.wv.vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)

#create scatter plot of projection
pyplot.scatter(result[:,0], result[:,1])
words = list(model.wv.vocab)
for i, word in enumerate(words):
    pyplot.annotate(word, xy=(result[i,0], result[i, 1]))
pyplot.show()
