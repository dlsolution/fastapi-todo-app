import sys
from loguru import logger

logger.remove()
logger.add(sys.stdout, colorize=True, enqueue=False)
