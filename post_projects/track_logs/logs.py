import logging
import sys

h = [
    logging.FileHandler("logs/log.log"),
    logging.StreamHandler(stream=sys.stdout)
]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=h
)

logger = logging.getLogger(__name__)


def track_logs(input_event):
    logging.info(input_event)

    
