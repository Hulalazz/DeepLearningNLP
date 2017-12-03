# Bag-of-Words Model

Definition: A way of extracting features from text for use in modeling. It is a representation of text that describes occurrence of words within a document. The model is concerned only with whether known words occur in the document, not where in the document.

Involves two things:
* A vocabulary of known words
* A measure of the presence of known words



## Ways of Scoring Words
Once vocabulary has been chosen, the occurrence of words in example documents need to be scored. Some ways of scoring are:
* Binary Scoring: scoring of presence of absence of words
* Counts: Count number of times each word appears in a document
* Frequencies: Calculate frequency that each word appears in document out of all words in document

## TF-IDF (Term Frequency-Inverse Document Frequency)
The problem: a problem with scoring word frequency is that highly frequent words start to dominate the document, leading to a higher score. This could be misleading because those words may not contain as much informational content to the model.

* Term Frequency: scoring of the frequency of the word in current document
* Inverse Document Frequency: scoring of how rare the word is across documents
