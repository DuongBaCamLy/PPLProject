rules = [
    {
        "event": "casual",
        "weather": "cold",
        "style": "minimal",
        "time": "evening",
        "output": "🌙 Áo len mỏng, quần kaki, sneaker."
    },
    {
        "event": "casual",
        "weather": "cold",
        "style": "minimal",
        "output": "🧥 Áo hoodie, quần jeans dài, sneaker."
    },
    {
        "event": "wedding",
        "weather": "cold",
        "style": "formal",
        "output": "👗 Áo vest, cổ lọ, áo khoác dày, giày da."
    }
]

def match_rule(user_input: dict):
    print("🔍 Input từ người dùng:", user_input)
    for rule in rules:
        print("🧪 So sánh với rule:", rule)
        matched = True
        for k, v in rule.items():
            if k != "output":
                if user_input.get(k) != v:
                    matched = False
                    print(f"❌ Không khớp: {k} = {user_input.get(k)} ≠ {v}")
                    break
        if matched:
            print("✅ KHỚP RULE:", rule)
            return rule["output"]
    print("❌ Không khớp rule nào.")
    return "❓ Chưa có gợi ý cho tổ hợp này."
