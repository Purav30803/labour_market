import re

STOPWORDS = set(["the", "and", "in", "to", "of", "for", "a", "an", "on", "with", "is", "be"])

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return ' '.join([word for word in text.split() if word not in STOPWORDS])
