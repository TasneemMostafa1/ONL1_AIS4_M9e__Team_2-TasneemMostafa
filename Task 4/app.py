import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
nltk.download('stopwords')
nltk.download('punkt') 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

################################################################
tweets_df = pd.read_csv("train.csv")
tweets_df = tweets_df[['text', 'sentiment']]

test_df = pd.read_csv("test.csv")
test_df = test_df[['text', 'sentiment']]

# Remove empty or NaN rows from training data
tweets_df.dropna(subset=['text'], inplace=True)
tweets_df = tweets_df[tweets_df['text'].str.strip() != '']
