import os
import time
import logging


class Logger:
    @staticmethod
    def log():
        file_path = os.path.join('logs', 'Automation_' + time.strftime("%Y%m%d-%H%M%S") + '.log')

        logger = logging.getLogger()
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler(file_path, "w", encoding="UTF-8")

        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        # Remove any existing handlers
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)

        # Add handlers to the logger
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

        logger.setLevel(logging.INFO)  # Set the logger level to INFO

        return logger
