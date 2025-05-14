import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import os

def train_model():
    # Enhanced dataset for sentiment analysis
    texts = [
        # Positive examples
        "I love this product, it's amazing!",
        "Great service and fast delivery",
        "Excellent customer support",
        "Best decision I've ever made",
        "Absolutely fantastic!",
        "This product exceeded my expectations",
        "Wonderful experience, highly recommended",
        "The quality is outstanding",
        "Very satisfied with my purchase",
        "Couldn't be happier with this product",
        
        # Negative examples
        "This is the worst experience ever",
        "Terrible quality, would not recommend",
        "Very disappointed with the purchase",
        "Complete waste of money",
        "Not worth the price at all",
        "Poor customer service",
        "The product broke after one day",
        "Extremely dissatisfied",
        "Regret buying this",
        "Awful experience, stay away"
    ]
    labels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  # Positive labels
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Negative labels

    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

    vectorizer = TfidfVectorizer(
        max_features=1000,
        ngram_range=(1, 2),  # Use both unigrams and bigrams
        stop_words='english'
    )
    X_train_vec = vectorizer.fit_transform(X_train)

    model = LogisticRegression(
        C=1.0,
        class_weight='balanced',  # Handle class imbalance
        max_iter=1000
    )
    model.fit(X_train_vec, y_train)

    os.makedirs('app/model/saved', exist_ok=True)
    joblib.dump(model, 'app/model/saved/model.joblib')
    joblib.dump(vectorizer, 'app/model/saved/vectorizer.joblib')
    
    X_test_vec = vectorizer.transform(X_test)
    accuracy = model.score(X_test_vec, y_test)
    print(f"Model accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    train_model() 