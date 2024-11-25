import logging

class Logger:
    """
    Logger class for managing chatbot interaction logs and errors.
    Logs interactions to a file for debugging and analysis.
    """
    def __init__(self, log_file="chatbot.log"):
        """
        Initializes the Logger with a specified log file.

        Args:
            log_file (str): Path to the log file.
        """
        self.log_file = log_file
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

    def log_interaction(self, user_input, intent, entities, response):
        """
        Logs a chatbot interaction.

        Args:
            user_input (str): The user's input message.
            intent (str): The classified intent of the user input.
            entities (dict): The extracted entities from the user input.
            response (str): The chatbot's response.
        """
        entities_str = ", ".join(f"{key}: {value}" for key, value in entities.items())
        log_message = (
            f"User Input: {user_input} | Intent: {intent} | "
            f"Entities: {entities_str} | Response: {response}"
        )
        logging.info(log_message)

    def log_error(self, error_message):
        """
        Logs an error message.

        Args:
            error_message (str): The error message to log.
        """
        logging.error(f"Error: {error_message}")


if __name__ == "__main__":
    # Example usage of the Logger class
    logger = Logger()

    # Log an interaction
    logger.log_interaction(
        user_input="Where is my refund?",
        intent="REFUND_REQUEST",
        entities={"ORDER_ID": "98765"},
        response="I can assist you with a refund. Could you provide additional details?"
    )

    # Log an error
    logger.log_error("Failed to process user input due to NLP error.")
