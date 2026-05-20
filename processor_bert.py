import sys
import joblib
from sentence_transformers import SentenceTransformer

# Load the pre-trained BERT model and the trained classifier
transformer_model = SentenceTransformer('all-MiniLM-L6-v2')
# Load the trained classifier
classifier = joblib.load('model.joblib')

def classify_with_bert(log_message):
    # compute the embedding for the log message
    message_embedding = transformer_model.encode(log_message)
    # Make a prediction ensure the classifier receives a 2D array of embeddings
    probabilty = classifier.predict_proba([message_embedding])[0]
    if max(probabilty)< 0.5:
        return "Unclassified"
    prediction = classifier.predict([message_embedding])[0]
    return prediction

if __name__ == "__main__":
    logs = [
        'alpha.osapi_compute.wsgi.server - 12.10.11.1 API returned 404 not found error',
        'GET /v2/3454/servers/detail HTTP/1.1 RCODE 404 len:124 time: 2.3543',
        "System crashed",
        "Hey bro, chill yeah"
    ]
    for log in logs:
        label = classify_with_bert(log)
        print(f"Log message: {log} ==> {label}")
