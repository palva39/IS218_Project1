import os
import logging
from app.repl import REPL
from app.history_manager import HistoryManager
from app.plugin_loader import PluginLoader
from dotenv import load_dotenv

def setup_logging():
    """Configure logging based on environment variables."""
    load_dotenv()  # Load environment variables from a .env file if present
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    logging.basicConfig(
        level=getattr(logging, log_level, logging.INFO),
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def main():
    # Setup logging configuration
    setup_logging()

    # Display startup message
    logging.info("Starting the Advanced Python Calculator...")

    # Initialize REPL and start the calculator
    repl = REPL()
    repl.start()

if __name__ == "__main__":
    main()
