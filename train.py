import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the dataset
df = pd.read_csv("data/train.csv")

# Separate features (X) and target variable (y)
X = df.drop(columns=['Disease'])
y = df['Disease']

# Initialize the RandomForestClassifier
model = RandomForestClassifier()

# Train the model
model.fit(X, y)

# Save the trained model to a file
with open("model.pkl", 'wb') as f:
    pickle.dump(model, f)