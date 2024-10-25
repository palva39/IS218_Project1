import logging
import os

def setup_logging():
    """Sets up logging configuration using environment variables."""

    # Get logging level and output from environment variables
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()  # Default to INFO if not set
    log_file = os.getenv('LOG_FILE', None)  # File to log to, if set
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    
    # Configure the logging level based on the environment variable
    numeric_level = getattr(logging, log_level, logging.INFO)
    
    # Basic configuration
    if log_file:
        logging.basicConfig(
            level=numeric_level,
            format=log_format,
            filename=log_file,
            filemode='a'  # Append to the log file
        )
    else:
        logging.basicConfig(
            level=numeric_level,
            format=log_format
        )

# Initialize logging at the start of the application
setup_logging()
