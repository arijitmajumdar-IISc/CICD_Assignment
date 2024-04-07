import pandas as pd
from sklearn.ensemble import RandomForestClassifier  # Import RandomForestClassifier
import pickle
import numpy as np

# Load your data
df = pd.read_csv("data/test.csv")
X = df.drop(columns=['Disease']).to_numpy()
y = df['Disease'].to_numpy()

# Initialize and fit the Random Forest model
model = RandomForestClassifier(n_estimators=100, max_depth=10)  # Adjust hyperparameters as needed
model.fit(X, y)

# Evaluate the model
print(round(model.score(X, y), 3))
