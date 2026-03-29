\# Sentiment Analysis Tool (CSV Processing)



\## Overview

This project performs basic sentiment analysis on text data from a CSV file.



It reads input data, analyzes each text entry using a pre-trained sentiment model (VADER), and outputs results with sentiment labels.



\---



\## Features

\- CSV input → CSV output

\- Sentiment classification (Positive / Neutral / Negative)

\- Uses pre-trained NLP model (no training required)

\- Simple and fast processing



\---



\## Tech Stack

\- Python

\- pandas

\- nltk (VADER sentiment analyzer)



\---



\## How It Works

1\. Load CSV file with a text column

2\. Analyze each text entry

3\. Assign sentiment label

4\. Save results to a new CSV file



\---



\## Input Example

Column required:

\- `review`



\---



\## Output Example

New column added:

\- `sentiment`



\---



\## Setup



Install dependencies:



```bash

pip install pandas nltk

```



Run:



python main.py
