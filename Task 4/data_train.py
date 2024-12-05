import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
import os
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json
from sklearn.decomposition import PCA


# Ensure nltk dependencies are downloaded
# nltk.download('stopwords')
# nltk.download('punkt')

# Define paths
OUT_DATA_PATH = os.path.join(os.getcwd(), 'outs')
os.makedirs(OUT_DATA_PATH, exist_ok=True)

MODEL_FILE_PATH = os.path.join(OUT_DATA_PATH, 'Train_prep.csv')
Train = pd.read_csv(MODEL_FILE_PATH)

MODEL_FILE_PATH = os.path.join(OUT_DATA_PATH, 'Test_prep.csv')
Test = pd.read_csv(MODEL_FILE_PATH)



MODEL_FILE_PATH = os.path.join(OUT_DATA_PATH, 'Train_process.csv')
message = pd.read_csv(MODEL_FILE_PATH)

MODEL_FILE_PATH = os.path.join(OUT_DATA_PATH, 'Test_process.csv')
message2 = pd.read_csv(MODEL_FILE_PATH)

# Split data
xtrain, xtest, ytrain, ytest = train_test_split(message, Train.sentiment, test_size=0.20, random_state=20)





pca = PCA(n_components=500)  # Reduce to 500 components (adjust as necessary)
xtrain = pca.fit_transform(xtrain)
xtest = pca.transform(xtest)
message2 = pca.transform(message2)




# Train the SVM model
svc_model = SVC(C=0.2, kernel='linear', gamma=0.8)
svc_model.fit(xtrain, ytrain)

# Evaluate on training data
train_pred = svc_model.predict(xtrain)
print("Training Data Classification Report:\n", classification_report(ytrain, train_pred))
train_accuracy = accuracy_score(ytrain, train_pred)
print("Training Data Accuracy:", train_accuracy)

# Evaluate on test data
test_pred = svc_model.predict(xtest)
print("Testing Data Classification Report:\n", classification_report(ytest, test_pred))
test_accuracy = accuracy_score(ytest, test_pred)
print("Testing Data Accuracy:", test_accuracy)


# Predict on new test data
test_pred_new = svc_model.predict(message2)
print("Test Data Classification Report (New Data):\n", classification_report(Test['sentiment'], test_pred_new))
test_accuracy_new = accuracy_score(Test['sentiment'], test_pred_new)
print("Test Data Accuracy (New Data):", test_accuracy_new)

# Save the model
model_path = 'Models/svm_model1.pkl'
joblib.dump(svc_model, model_path)

# Save metrics to metrics.json
metrics = {
    "train_accuracy": train_accuracy,
    "test_accuracy": test_accuracy,
    "test_accuracy_new": test_accuracy_new
}

metrics_path = "metrics.json"
with open(metrics_path, "w") as f:
    json.dump(metrics, f)

print(f"Metrics saved to {metrics_path}")
print(f"Model saved to {model_path}")
