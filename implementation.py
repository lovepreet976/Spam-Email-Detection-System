from sklearn.model_selection import train_test_split

# Split the dataset into features (X) and labels (y)
X = padded_sequences
y = data[57]  # Assuming the label (spam/ham) is in the last column

# Split into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model.fit(X_train, y_train, epochs=5, batch_size=64, validation_data=(X_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test accuracy: {accuracy:.2f}')
