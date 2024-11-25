from chatbot import Chatbot

def main():
    """
    Main function to run the chatbot.
    """
    print("Welcome to the AI Chatbot!")
    print("Type 'exit' to end the chat.")

    # Instantiate the Chatbot
    bot = Chatbot()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Get response from chatbot
        response = bot.process_input(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
