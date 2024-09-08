import logging

# 设置logger
logger = logging.getLogger(__name__)
starem_handler = logging.StreamHandler()
file_handler = logging.FileHandler('plugin.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
starem_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(starem_handler)
logger.addHandler(file_handler)
file_handler.setLevel(logging.DEBUG)
starem_handler.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
