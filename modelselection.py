from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D

# Define the model architecture
model = Sequential()
model.add(Embedding(input_dim=5000, output_dim=128, input_length=max_length))  # Embedding layer
model.add(SpatialDropout1D(0.2))  # Dropout layer to prevent overfitting
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))  # LSTM layer
model.add(Dense(1, activation='sigmoid'))  # Output layer for binary classification

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
