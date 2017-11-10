from keras.preprocessing.text import Tokenizer

#define documents
docs = ['Well done!',
        'Good work!',
        'Great effort',
        'nice work',
        'Excellent']

#create Tokenizer
t = Tokenizer()

#fit tokenizer on the documents
t.fit_on_texts(docs)

#summarize learnings
print(t.word_counts)
print(t.document_count)
print(t.word_index)
print(t.word_docs)

#integer encode documents
encoded_docs = t.texts_to_matrix(docs, mode='count')
print(encoded_docs)
