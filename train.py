import pandas as pd
import non-existing-module
from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np

df = pd.read_csv("data/train.csv")
X = df.drop(columns=['Disease']).to_numpy()
y = df['Disease'].to_numpy()
labels = np.sort(np.unique(y))
y = np.array([np.where(labels == x) for x in y]).flatten()

# Initialize the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit the model to the data
model.fit(X, y)

# Save the trained model to a file
with open("model.pkl", 'wb') as f:
    pickle.dump(model, f)