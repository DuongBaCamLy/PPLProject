import random

facts = [
    {
        "conditions": {
            "gender": "female",
            "event": "casual",
            "weather": "cold",
            "style": "minimal",
            "time": "evening"
        },
        "outfit": "Wool coat, long dress, high heels."
    },
    {
        "conditions": {
            "gender": "male",
            "event": "wedding",
            "weather": "hot",
            "style": "formal",
            "time": "afternoon"
        },
        "outfit": "White shirt, light-colored trousers, brown leather shoes, and sunglasses."
    },
    {
        "conditions": {
            "gender": "female",
            "event": "interview",
            "weather": "sunny",
            "style": "formal",
            "time": "morning"
        },
        "outfit": "White shirt, pencil skirt, flats, and a work handbag."
    },
    {
        "conditions": {
            "gender": "male",
            "event": "casual",
            "weather": "rainy",
            "style": "sporty",
            "time": "evening"
        },
        "outfit": "Waterproof hoodie, joggers, sneakers, and baseball cap."
    },
    {
        "conditions": {
            "gender": "female",
            "event": "wedding",
            "weather": "sunny",
            "style": "formal",
            "time": "afternoon"
        },
        "outfit": "Short-sleeved midi dress, high heels, and a small handbag."
    },
    {
        "conditions": {
            "gender": "male",
            "event": "interview",
            "weather": "cold",
            "style": "formal",
            "time": "morning"
        },
        "outfit": "White shirt, gray blazer, black trousers, and oxford shoes."
    },
    {
        "conditions": {
            "gender": "female",
            "event": "casual",
            "weather": "hot",
            "style": "streetwear",
            "time": "afternoon"
        },
        "outfit": "Crop top, denim shorts, sneakers, and sunglasses."
    },
    {
        "conditions": {
            "gender": "male",
            "event": "casual",
            "weather": "sunny",
            "style": "minimal",
            "time": "morning"
        },
        "outfit": "White T-shirt, khaki shorts, and slip-on shoes."
    },
    {
        "conditions": {
            "gender": "female",
            "event": "interview",
            "weather": "rainy",
            "style": "minimal",
            "time": "morning"
        },
        "outfit": "Long-sleeve shirt, dark fabric trousers, closed flats, and a light jacket."
    },
    {
        "conditions": {
            "gender": "male",
            "event": "casual",
            "weather": "cold",
            "style": "streetwear",
            "time": "night"
        },
        "outfit": "Bomber jacket, black T-shirt, ripped jeans, and high-top sneakers."
    },
    {
        "conditions": {
            "gender": "female",
            "event": "wedding",
            "weather": "cool",
            "style": "minimal",
            "time": "evening"
        },
        "outfit": "Pastel long-sleeve dress, light jacket, and pointed high heels."
    }
]

def logical_query(user_input: dict, threshold: int = 3):
    best_fact = None
    best_score = 0

    for fact in facts:
        conditions = fact["conditions"]
        score = sum(
            1 for k, v in conditions.items()
            if user_input.get(k) == v
        )
        if score > best_score and score >= threshold:
            best_score = score
            best_fact = fact

    if best_fact:
        return best_fact["outfit"]
    return "No suggestion available for this combination."
