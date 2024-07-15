import nltk
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by OpenAI. You can call me Chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, no problem",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great!",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, I don't have an age.",]
    ],
    [
        r"what (.*) want ?",
        ["I just want to chat with you!",]
    ],
    [
        r"(.*) created ?",
        ["I was created by a team of developers at OpenAI.",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am based in the cloud, but I can chat with you from anywhere.',]
    ],
    [
        r"how is the weather in (.*)?",
        ["Weather in %1 is always unpredictable.",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a big fan of AI-related activities.",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon!", "It was nice talking to you. Goodbye!"]
    ],
]

# Default responses when the chatbot doesn't understand the input
default_responses = ["I am sorry, I don't understand that.", "Could you please rephrase that?", "I'm not sure I get what you mean."]

# Create a chat object
chatbot = Chat(pairs, reflections)

def chat():
    print("Hi, I'm a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Bye, take care!")
            break
        response = chatbot.respond(user_input)
        if response:
            print("Chatbot:", response)
        else:
            print("Chatbot:", default_responses[0])

if __name__ == "__main__":
    chat()
