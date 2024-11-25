# response_handler.py

class ResponseHandler:
    """
    ResponseHandler generates responses based on user intent and extracted entities.
    It uses predefined templates for simplicity and can be extended to include
    dynamic data fetching or API integrations.
    """
    def __init__(self):
        """
        Initializes the ResponseHandler with a dictionary of response templates.
        """
        self.response_templates = {
            "ORDER_STATUS": "It looks like you want to check the status of your order. Can you provide the order number?",
            "HELP": "Sure, I'm here to help! Please let me know your question or issue.",
            "REFUND_REQUEST": "I can assist you with a refund. Could you please share your order details or the reason for the refund?",
            "UNKNOWN": "I'm sorry, I didn't quite understand that. Could you rephrase your question or provide more details?"
        }

    def generate_response(self, intent, entities):
        """
        Generates a response based on the provided intent and entities.

        Args:
            intent (str): The classified intent of the user input.
            entities (dict): The extracted entities from the user input.

        Returns:
            str: A response string tailored to the user's query.
        """
        # Fetch response template based on intent
        response = self.response_templates.get(intent, "I'm not sure how to help with that.")
        
        # Add entity-specific information to the response if applicable
        if entities and intent in ["ORDER_STATUS", "REFUND_REQUEST"]:
            entity_details = self.format_entities(entities)
            response += f" Here are the details I found: {entity_details}"

        return response

    def format_entities(self, entities):
        """
        Formats extracted entities into a readable string.

        Args:
            entities (dict): The extracted entities.

        Returns:
            str: A formatted string of entity details.
        """
        return ", ".join(f"{label}: {value}" for label, value in entities.items())


if __name__ == "__main__":
    # Example usage of the ResponseHandler class
    handler = ResponseHandler()

    # Simulated inputs for testing
    test_intents = ["ORDER_STATUS", "HELP", "REFUND_REQUEST", "UNKNOWN"]
    test_entities = [
        {"ORDER_ID": "12345", "DATE": "2023-11-01"},
        {},
        {"ORDER_ID": "98765"},
        {}
    ]

    for intent, entities in zip(test_intents, test_entities):
        print(f"Intent: {intent}")
        print(f"Entities: {entities}")
        print(f"Response: {handler.generate_response(intent, entities)}\n")
