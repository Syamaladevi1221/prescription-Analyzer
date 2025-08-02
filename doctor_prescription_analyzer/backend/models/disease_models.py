from transformers import pipeline

# Load only once
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

possible_diseases = [
    "cold", "fever", "infection", "pain", "diabetes", "hypertension", "headache", "cough"
]

def predict_disease(text: str):
    result = classifier(text, candidate_labels=possible_diseases)
    return result['labels'][0]  # Most likely disease
