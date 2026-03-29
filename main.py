import os
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon once
nltk.download("vader_lexicon")

# Get directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build full path to input.csv
file_path = os.path.join(BASE_DIR, "input.csv")

# Read CSV
df = pd.read_csv(file_path)

# Preview data
print("Preview of data:")
print(df.head())

# Check column exists
if "review" not in df.columns:
    raise ValueError("Column 'review' not found in CSV")

print("\nColumn 'review' found.")

# Create sentiment analyzer
sia = SentimentIntensityAnalyzer()


def classify_sentiment(text: str) -> str:
    """Convert VADER compound score into sentiment label."""
    scores = sia.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"


# Convert review values to strings and apply sentiment classification
df["sentiment"] = df["review"].fillna("").astype(str).apply(classify_sentiment)

print("\nPreview with sentiment:")
print(df[["review", "sentiment"]].head())

# Save result to new CSV file
output_path = os.path.join(BASE_DIR, "output.csv")
df.to_csv(output_path, index=False)

print(f"\nFile saved to: {output_path}")