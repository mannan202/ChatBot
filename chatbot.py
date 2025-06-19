import re
import random

# Define patterns and responses
patterns = {
    r'\b(hi|hello|hey)\b': [
        "Hello! How can I assist you today?",
        "Hi there! I'm ready to help.",
    ],
    r'how are you': [
        "I'm doing great, thanks for asking!",
        "All systems are operational!",
    ],
    r'\b(bye|exit|quit)\b': [
        "Goodbye! Have a wonderful day.",
        "See you later!",
    ]
}

# Knowledge base with lowercase keys for fast matching
knowledge_base = {
    "your name": "I'm ChatBot, your AI assistant.",
    "what is your name": "I'm ChatBot, your AI assistant.",
    "who are you": "I'm ChatBot, created to help you!",
    "who created you": "A developer who loves Python built me.",
    "what is python": "Python is a popular programming language known for its simplicity.",
    "what is ai": "AI stands for Artificial Intelligence—machines that simulate human thinking.",
    "what is machine learning": "Machine Learning is a subset of AI where machines learn from data.",
    "what is your purpose": "I'm here to chat with you and answer basic questions.",
    "what is the capital of bangladesh": "The capital of Bangladesh is Dhaka.",
    "how old are you": "I don't have an age, but I'm always up-to-date!",
}

# Evaluate arithmetic expression
def evaluate_expression(expr):
    try:
        result = eval(expr, {"__builtins__": None}, {})
        return f"The result is {result}"
    except Exception:
        return "Sorry, I couldn't evaluate that expression."

# Extract arithmetic expression from user input
def extract_arithmetic_expression(text):
    match = re.search(r'([\d\.\s\+\-\*\/\(\)]+)', text)
    return match.group(1).strip() if match else None

# Match user input to pattern or knowledge base
def match_pattern(user_input):
    expr = extract_arithmetic_expression(user_input)
    if expr:
        return evaluate_expression(expr)

    # Match patterns
    for pattern, responses in patterns.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses)

    # Match knowledge base
    cleaned_input = user_input.lower()
    for key, value in knowledge_base.items():
        if key in cleaned_input:
            return value

    return "I'm not sure how to respond to that."

# Main chatbot loop
def chatbot():
    print("ChatBot: Hello! Ask me anything, including math. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("ChatBot: Goodbye! 👋")
            break

        response = match_pattern(user_input)
        print("ChatBot:", response)

# Run chatbot
if __name__ == "__main__":
    chatbot()
