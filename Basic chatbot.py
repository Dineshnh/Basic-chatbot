import nltk
from nltk.chat.util import Chat, reflections
patterns = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm doing well, thank you!", "I'm good, thanks for asking."]),
    (r"what is your name?", ["You can call me Chatbot.", "I'm Chatbot, nice to meet you!"]),
    (r"bye|goodbye", ["Goodbye!", "See you later!", "Bye!"]),
]
chatbot = Chat(patterns, reflections)

# start the chat
def start_chat():
    print("Welcome to the Chatbot! Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

# Main function
def main():
    # Download NLTK resources (if not already downloaded)
    nltk.download('punkt')
    nltk.download('wordnet')
    
    start_chat()

if __name__ == "__main__":
    main()