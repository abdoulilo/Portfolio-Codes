from nlp_processor import NLPProcessor
from response_handler import ResponseHandler
from logger import Logger


class Chatbot:
    """
    Chatbot class orchestrates NLP processing, response generation, and logging.
    """
    def __init__(self):
        """
        Initializes the chatbot with its NLPProcessor, ResponseHandler, and Logger components.
        """
        self.nlp_processor = NLPProcessor()
        self.response_handler = ResponseHandler()
        self.logger = Logger()

    def process_input(self, user_input):
        """
        Processes the user input, generates a response, and logs the interaction.

        Args:
            user_input (str): The input from the user.

        Returns:
            str: The chatbot's response.
        """
        # Analyze the user input using NLPProcessor
        intent, entities = self.nlp_processor.analyze_input(user_input)

        # Generate a response using ResponseHandler
        response = self.response_handler.generate_response(intent, entities)

        # Log the interaction (ensure all required arguments are provided)
        self.logger.log_interaction(
            user_input=user_input,
            intent=intent,
            entities=entities,
            response=response
        )

        return response


if __name__ == "__main__":
    # Example usage of the Chatbot
    bot = Chatbot()
    print("Welcome to the AI Chatbot!")
    print("Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = bot.process_input(user_input)
        print(f"Chatbot: {response}")
