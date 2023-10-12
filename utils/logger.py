import os
import time
import logging

import pyautogui


class Logger:
    @staticmethod
    def log():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, ".."))
        file_path = os.path.join(project_root, 'logs', 'Automation_' + time.strftime("%Y%m%d-%H%M%S") + '.log')

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

    @staticmethod
    def take_screenshot(test_name):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, ".."))
        screenshot_path = os.path.join(project_root, 'logs', 'screenshots', f'{test_name}.png')
        pyautogui.screenshot(screenshot_path)
