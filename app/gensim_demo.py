import gensim.downloader as api
import numpy as np
# Load pre-trained Word2Vec model
w2v_model = api.load("word2vec-google-news-300")

# Define input sentence
input_sentence = "The quick brown fox jumps over the lazy dog."

# Convert sentence to list of words
words = input_sentence.split()

# Convert each word to its vector representation
vectors = [w2v_model[word] for word in words if word in w2v_model.vocab]

# Concatenate the vectors to form a single sentence vector
sentence_vector = np.concatenate(vectors, axis=0)

# Print the sentence vector
print(sentence_vector)
