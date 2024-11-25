# nlp_processor.py

import spacy

class NLPProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            raise RuntimeError("SpaCy language model 'en_core_web_sm' is not installed. "
                               "Install it with: python -m spacy download en_core_web_sm")

    def analyze_input(self, text):
        """
        Analyzes the user input to extract intent and entities.

        Args:
            text (str): The user input string.

        Returns:
            tuple: A tuple containing the classified intent (str) and
                   extracted entities (dict).
        """
        doc = self.nlp(text)
        intent = self.classify_intent(doc)
        entities = self.extract_entities(doc)
        return intent, entities

    def classify_intent(self, doc):
        """
        Classifies the user's intent based on the text.

        Args:
            doc (spacy.tokens.Doc): A spaCy Doc object created from user input.

        Returns:
            str: The classified intent.
        """
        # Example of simple intent classification using keyword matching
        text = doc.text.lower()
        if "order" in text:
            return "ORDER_STATUS"
        elif "help" in text or "support" in text:
            return "HELP"
        elif "refund" in text or "return" in text:
            return "REFUND_REQUEST"
        else:
            return "UNKNOWN"

    def extract_entities(self, doc):
        """
        Extracts named entities from the user's input.

        Args:
            doc (spacy.tokens.Doc): A spaCy Doc object created from user input.

        Returns:
            dict: A dictionary of extracted entities with labels as keys and
                  entity text as values.
        """
        entities = {}
        for ent in doc.ents:
            entities[ent.label_] = ent.text
        return entities


if __name__ == "__main__":
    # Example usage of the NLPProcessor class
    processor = NLPProcessor()
    while True:
        user_input = input("Enter a message (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting NLP Processor.")
            break
        intent, entities = processor.analyze_input(user_input)
        print(f"Intent: {intent}")
        print(f"Entities: {entities}")
