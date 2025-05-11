import re

# Mapping tiếng Việt sang DSL
mappings = {
    "gender": {
        "nam": "male", "con trai": "male", "mình là nam": "male", "tôi là nam": "male",
        "nữ": "female", "con gái": "female", "mình là nữ": "female", "tôi là nữ": "female"
    },
    "weather": {
        "lạnh": "cold", "rét": "cold", "se lạnh": "cold",
        "nóng": "hot", "oi bức": "hot",
        "mưa": "rainy", "trời mưa": "rainy",
        "nắng": "sunny", "trời nắng": "sunny"
    },
    "time": {
        "sáng": "morning", "buổi sáng": "morning",
        "chiều": "afternoon", "buổi chiều": "afternoon",
        "tối": "evening", "buổi tối": "evening",
        "đêm": "night", "ban đêm": "night"
    },
    "event": {
        "đám cưới": "wedding", "tiệc cưới": "wedding", "cưới": "wedding",
        "phỏng vấn": "interview", "xin việc": "interview",
        "đi chơi": "casual", "cafe": "casual"
    },
    "style": {
        "tối giản": "minimal", "đơn giản": "minimal",
        "trang trọng": "formal", "lịch sự": "formal",
        "đường phố": "streetwear", "cá tính": "streetwear",
        "thể thao": "sporty", "năng động": "sporty"
    }
}

def extract_field(text, field):
    for vi, dsl in mappings[field].items():
        if vi in text.lower():
            return dsl
    return None

def extract_location(text):
    match = re.search(r"(ở|tại)\s+([a-zA-ZÀ-Ỹà-ỹ]+)", text)
    if match:
        return match.group(2).lower()
    return None

def vn_to_dsl(text):
    fields = {}
    for field in mappings:
        value = extract_field(text, field)
        if value:
            fields[field] = value
    loc = extract_location(text)
    if loc:
        fields["location"] = loc

    # Convert sang DSL outfit(...)
    dsl = "outfit(" + ", ".join([f"{k}={v}" for k, v in fields.items()]) + ")"
    return dsl

if __name__ == "__main__":
    text = "Tôi là con gái, trời lạnh, đi đám cưới ở Đà Lạt, phong cách tối giản"
    print(vn_to_dsl(text))

