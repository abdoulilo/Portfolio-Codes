# config.py

class Config:
    """
    Config class holds configuration settings for the chatbot application.
    Modify values here to adjust the chatbot's behavior and environment.
    """
    # General Configurations
    BOT_NAME = "AI Chatbot"
    VERSION = "1.0.0"

    # Logging Configuration
    LOG_FILE = "chatbot.log"

    # CSV Storage Configuration
    CSV_FILE = "chatbot_interactions.csv"

    # NLP Configuration
    DEFAULT_LANGUAGE_MODEL = "en_core_web_sm"

    # Other Settings
    MAX_RECENT_INTERACTIONS = 10
    DEBUG_MODE = True

if __name__ == "__main__":
    # Example usage of the Config class
    print(f"Chatbot Name: {Config.BOT_NAME}")
    print(f"Log File: {Config.LOG_FILE}")
    print(f"CSV File: {Config.CSV_FILE}")
    print(f"Debug Mode: {Config.DEBUG_MODE}")
