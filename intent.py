from transformers import pipeline

intent_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_intent(query, candidate_labels):
    result = intent_classifier(query, candidate_labels)
    return result

def check_intent_score(intent_result, threshold=0.4):
    for label, score in zip(intent_result['labels'], intent_result['scores']):
        if score > threshold:
            return True
    return False
