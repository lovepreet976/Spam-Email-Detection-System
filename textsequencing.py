from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# Initialize the tokenizer
tokenizer = Tokenizer(num_words=5000)  # Limit to top 5000 words
tokenizer.fit_on_texts(data[0])  # Fit on the cleaned email texts

# Convert texts to sequences
sequences = tokenizer.texts_to_sequences(data[0])

# Padding sequences to ensure they are all the same length
max_length = 100  # Maximum length of sequences
padded_sequences = pad_sequences(sequences, maxlen=max_length)
