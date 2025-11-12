import os
import sys
import logging

# This is cnnClassifier package's constructor file. We setup logging here instead of creating a separate logging module.

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # Logs msgs to a file at log_filepath
        logging.StreamHandler(sys.stdout)  # Logs same msgs to terminal as well
    ]
)

logger = logging.getLogger("cnnClassifierLogger")
