import json
import os

# Load JSON data
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def find_answer(user_input):
    """Find an answer by matching user input with keywords."""
    user_input = user_input.lower()
    best_match = None
    highest_match_count = 0

    for item in data["data"]:
        match_count = sum(1 for kw in item["keywords"] if kw.lower() in user_input)
        if match_count > highest_match_count:
            highest_match_count = match_count
            best_match = item["answer"]

    if best_match:
        return best_match
    else:
        # If not found, check if the input is about planning
        for section, content in data["ChatbotPlanning"].items():
            if any(word in user_input for word in section.lower().split("_")):
                return f"{section.replace('_', ' ')}:\n" + "\n".join(f"- {q}" for q in content["questions"])
        return "I'm not sure about that yet, but I'm learning more every day!"

print("🤖 Chatbot Assistant — type 'exit' to stop")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! 👋")
        break
    answer = find_answer(user_input)
    print("Bot:", answer)
