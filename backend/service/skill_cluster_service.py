import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from utils.text_cleaning import clean_text
import os
import re

MODEL_DIR = os.path.dirname(__file__).replace("service", "models")

CLUSTER_LABELS = {
    0: "Sales & Customer Experience",
    1: "Operations & Program Management",
    2: "Cloud & Partner Ecosystem",
    3: "Internships & Early Career Roles",
    4: "Technical Cloud & Engineering",
    5: "Hardware, Design & Research"
}


# Load models once
with open(('models/kmeans_model.pkl'), "rb") as f:
    model = pickle.load(f)

with open('models/vectorizer.pkl', "rb") as f:
    vectorizer = pickle.load(f)



def is_valid_text(text: str) -> bool:
    text = text.lower()
    words = re.findall(r'\b[a-z]{3,}\b', text)  # words with at least 3 letters
    return len(words) >= 2  # allow at least 2 valid words


def predict_cluster(qualifications: str):
    if not is_valid_text(qualifications):
        return None, "Input doesn't appear to contain valid or enough skill-related content."

    cleaned = clean_text(qualifications)
    if len(cleaned.split()) < 2:
        return None, "Input too short. Please describe qualifications in more detail."

    vector = vectorizer.transform([cleaned])
    cluster = int(model.predict(vector)[0])
    cluster_label = CLUSTER_LABELS.get(cluster, f"Cluster {cluster}")
    return cluster, cluster_label
