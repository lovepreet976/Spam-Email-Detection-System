import pandas as pd
import scrubadub

# Load the Spambase dataset
data = pd.read_csv('spambase.data', header=None)

# Function to clean the email text
def clean_text(text):
    cleaned = scrubadub.clean(text)  # Clean sensitive info
    cleaned = cleaned.lower()  # Convert to lowercase
    return cleaned

# Apply the cleaning function to the email column (assumed to be the first column)
data[0] = data[0].apply(clean_text)
