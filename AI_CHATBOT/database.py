# database.py

import csv
import os
from datetime import datetime

class CSVDatabase:
    """
    CSVDatabase manages the storage and retrieval of chatbot interactions using a CSV file.
    """
    def __init__(self, file_path="chatbot_interactions.csv"):
        """
        Initializes the CSVDatabase and ensures the file exists with headers.

        Args:
            file_path (str): Path to the CSV file for storing interactions.
        """
        self.file_path = file_path
        self.headers = ["id", "user_input", "intent", "entities", "response", "timestamp"]
        self._initialize_csv()

    def _initialize_csv(self):
        """
        Ensures the CSV file exists and initializes it with headers if it is empty.
        """
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writeheader()

    def save_interaction(self, user_input, intent, entities, response):
        """
        Saves a chatbot interaction to the CSV file.

        Args:
            user_input (str): The user's input message.
            intent (str): The classified intent of the user input.
            entities (str): A stringified version of extracted entities (JSON or plain text).
            response (str): The chatbot's response.
        """
        timestamp = datetime.now().isoformat()
        new_id = self._get_next_id()

        with open(self.file_path, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writerow({
                "id": new_id,
                "user_input": user_input,
                "intent": intent,
                "entities": entities,
                "response": response,
                "timestamp": timestamp
            })

    def get_interactions(self, limit=10):
        """
        Retrieves recent chatbot interactions from the CSV file.

        Args:
            limit (int): The number of interactions to retrieve.

        Returns:
            list: A list of interactions as dictionaries.
        """
        interactions = []
        with open(self.file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            interactions = rows[-limit:]  # Get the last 'limit' rows

        return interactions

    def _get_next_id(self):
        """
        Determines the next ID for a new interaction.

        Returns:
            int: The next ID.
        """
        with open(self.file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            if not rows:
                return 1
            return int(rows[-1]["id"]) + 1

if __name__ == "__main__":
    # Example usage of the CSVDatabase class
    db = CSVDatabase()

    # Save an interaction
    db.save_interaction(
        user_input="What is the status of my order?",
        intent="ORDER_STATUS",
        entities='{"ORDER_ID": "12345"}',
        response="It looks like you want to check the status of your order."
    )

    # Retrieve and display interactions
    interactions = db.get_interactions()
    for interaction in interactions:
        print(interaction)
