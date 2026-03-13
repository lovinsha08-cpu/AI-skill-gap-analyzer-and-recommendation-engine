import os
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

# ✅ Make sure models folder exists
os.makedirs("models", exist_ok=True)

# Path to your EV ecosystem CSV
path=r"C:\Users\lovin\Downloads\ev_ecosystem_jobs.csv.csv"
df=pd.read_csv(path)



# Drop rows without Features
df = df.dropna(subset=["Features"])

# Columns
X = df["Features"]
y = df["Category"]

# TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words="english")
X_tfidf = tfidf.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

# Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model and vectorizer
pickle.dump(model, open("models/rf_classifier_categorization.pkl","wb"))
pickle.dump(tfidf, open("models/tfidf_vectorizer_categorization.pkl","wb"))

print("✅ Model trained successfully")
