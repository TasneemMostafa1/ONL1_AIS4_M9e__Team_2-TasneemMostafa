import pandas as pd
import os


OUT_DATA_PATH =os.path.join(os.getcwd(),'outs')
os.makedirs(OUT_DATA_PATH,exist_ok=True)

tweets_df = pd.read_csv("train.csv")
tweets_df = tweets_df[['text', 'sentiment']]

test_df = pd.read_csv("test.csv")
test_df = test_df[['text', 'sentiment']]

tweets_df.dropna(subset=['text'], inplace=True)
tweets_df = tweets_df[tweets_df['text'].str.strip() != '']


tweets_df.to_csv(os.path.join(OUT_DATA_PATH,'Train_prep.csv'),index=False);
test_df.to_csv(os.path.join(OUT_DATA_PATH,'Test_prep.csv'),index=False);