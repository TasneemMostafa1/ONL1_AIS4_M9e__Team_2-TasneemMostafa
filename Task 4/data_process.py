import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import string
from sklearn.feature_extraction.text import CountVectorizer
import os
 
 
OUT_DATA_PATH =os.path.join(os.getcwd(),'outs')
os.makedirs(OUT_DATA_PATH,exist_ok=True)
 
TRAIN_FILE_PATH =os.path.join(OUT_DATA_PATH,'Train_prep.csv')
train=pd.read_csv(TRAIN_FILE_PATH)

TEST_FILE_PATH = os.path.join(OUT_DATA_PATH, 'Test_prep.csv')
test = pd.read_csv(TEST_FILE_PATH)

def textClean(text):
    nopunc = [char.lower() for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    tokens = word_tokenize(nopunc)
    nohttp = [word for word in tokens if word[0:4] != 'http']
    nostop = [word for word in nohttp if word not in stopwords.words('english')]
    return nostop



vectorizer = CountVectorizer(analyzer=textClean)

message = vectorizer.fit_transform(train['text'])
message2 = vectorizer.transform(test['text'])

train = pd.DataFrame(message.toarray(), columns=vectorizer.get_feature_names_out())
test = pd.DataFrame(message2.toarray(), columns=vectorizer.get_feature_names_out())

train.to_csv(os.path.join(OUT_DATA_PATH,'Train_process.csv'),index=False);
test.to_csv(os.path.join(OUT_DATA_PATH,'Test_process.csv'),index=False);
