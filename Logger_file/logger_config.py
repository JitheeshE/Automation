
import logging
import os

# Create a logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Configure the logger
logger = logging.getLogger("PlaywrightLogger")
logger.setLevel(logging.INFO)

# Avoid adding duplicate handlers
if not logger.handlers:
    # Log messages to a file
    file_handler = logging.FileHandler("logs/test_execution.log")
    file_handler.setLevel(logging.INFO)

    # Define the log format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
