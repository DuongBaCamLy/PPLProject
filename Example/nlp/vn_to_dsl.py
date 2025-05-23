import re
import unicodedata
import string
import difflib

def normalize_text(text):
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

mappings = {
    "gender": {
        "male": "male", "boy": "male", "i am male": "male",
        "female": "female", "girl": "female", "i am female": "female"
    },
    "weather": {
        "cold": "cold", "chilly": "cold", "cool": "cold",
        "hot": "hot", "humid": "hot",
        "rain": "rainy", "rainy": "rainy",
        "sunny": "sunny", "bright": "sunny"
    },
    "time": {
        "morning": "morning",
        "afternoon": "afternoon",
        "evening": "evening",
        "night": "night"
    },
    "event": {
        "wedding": "wedding", "marriage": "wedding",
        "interview": "interview", "job application": "interview",
        "hangout": "casual", "coffee": "casual"
    },
    "style": {
        "minimal": "minimal", "simple": "minimal",
        "formal": "formal", "elegant": "formal",
        "streetwear": "streetwear", "urban": "streetwear",
        "sporty": "sporty", "active": "sporty"
    }
}

def extract_field(text, field):
    text = text.lower()
    for key, dsl in mappings[field].items():
        if key in text.lower():
            return dsl
    words = text.split()
    candidates = list(mappings[field].keys())
    for word in words:
        close = difflib.get_close_matches(word, candidates, n = 1, cutoff=0.8)
        if close:
            return mappings[field][close[0]]
    return None

def extract_location(text):
    match = re.search(r"(at|in)\s+([a-zA-Z\s]+)", text)
    if match:
        return match.group(2).strip().lower()
    return None

def vn_to_dsl(text):
    text = normalize_text(text)
    fields = {}
    for field in mappings:
        value = extract_field(text, field)
        if value:
            fields[field] = value
    loc = extract_location(text)
    if loc:
        fields["location"] = loc
    dsl = "outfit(" + ", ".join(map(lambda kv: f"{kv[0]}={kv[1]}", fields.items())) + ")"
    return dsl

if __name__ == "__main__":
    text = "I am a girl, it's cold, going to a wedding in Da Lat, minimal style"
    print(vn_to_dsl(text))
