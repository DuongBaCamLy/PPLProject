import random

rules = [
    {
        "gender": "female",
        "event": "casual",
        "weather": "cold",
        "style": "minimal",
        "time": "evening",
        "output": [
                "Áo khoác dạ, đầm dài, giày cao gót.",
                "Áo blazer, đầm midi, giày bốt.",
                "Áo cardigan, váy satin, giày cao gót.",
                "Áo len oversize, quần jeans dài, giày sneaker trắng và túi đeo chéo nhỏ."
]

    },
    {
        "gender": "male",
        "event": "wedding",
        "weather": "hot",
        "style": "formal",
        "time": "afternoon",
        "output": "Sơ mi trắng, quần tây màu sáng, giày da nâu và kính râm."
    },
    {
        "gender": "female",
        "event": "interview",
        "weather": "sunny",
        "style": "formal",
        "time": "morning",
        "output": "Áo sơ mi trắng, chân váy bút chì, giày búp bê và túi công sở."
    },
    {
        "gender": "male",
        "event": "casual",
        "weather": "rainy",
        "style": "sporty",
        "time": "evening",
        "output": "Áo hoodie chống thấm, quần jogger, sneaker và nón lưỡi trai."
    },
    {
        "gender": "female",
        "event": "wedding",
        "weather": "sunny",
        "style": "formal",
        "time": "afternoon",
        "output": "Đầm midi tay ngắn, giày cao gót và túi xách nhỏ gọn."
    },
    {
        "gender": "male",
        "event": "interview",
        "weather": "cold",
        "style": "formal",
        "time": "morning",
        "output": "Áo sơ mi trắng, blazer xám, quần tây đen và giày oxford."
    },
    {
        "gender": "female",
        "event": "casual",
        "weather": "hot",
        "style": "streetwear",
        "time": "afternoon",
        "output": "Áo crop top, quần short jeans, giày sneaker và kính mát."
    },
    {
        "gender": "male",
        "event": "casual",
        "weather": "sunny",
        "style": "minimal",
        "time": "morning",
        "output": "Áo thun trắng, quần short kaki và giày slip-on."
    },
    {
        "gender": "female",
        "event": "interview",
        "weather": "rainy",
        "style": "minimal",
        "time": "morning",
        "output": "Áo sơ mi dài tay, quần vải tối màu, giày bệt kín mũi và áo khoác mỏng."
    },
    {
        "gender": "male",
        "event": "casual",
        "weather": "cold",
        "style": "streetwear",
        "time": "night",
        "output": "Áo khoác bomber, áo thun đen, quần jeans rách và giày sneaker cổ cao."
    },
    {
        "gender": "female",
        "event": "wedding",
        "weather": "cool",
        "style": "minimal",
        "time": "evening",
        "output": "Váy dài tay màu pastel, áo khoác mỏng và giày cao gót mũi nhọn."
    }
]


def match_rule(user_input: dict):
    for rule in rules:
        matched = all(user_input.get(k) == v for k, v in rule.items() if k != "output")
        if matched:
            output = rule["output"]
            if isinstance(output, list):
                selected = random.sample(output, k=min(3, len(output)))
                return "\n".join([f"Option {i+1}: {item}" for i, item in enumerate(selected)])
            else:
                return output
    return "Chưa có gợi ý cho tổ hợp này."
