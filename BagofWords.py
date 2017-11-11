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
print("Word Counts: " + str(t.word_counts))
print("Document Count: " + str(t.document_count))
print("Word Index " + str(t.word_index))
print("Word Docs: " + str(t.word_docs))

#integer encode documents
encoded_docs = t.texts_to_matrix(docs, mode='count')
print("Integer encoded documents: \n")
print(encoded_docs)
