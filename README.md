# General Information
This project encompasses API and UI tests created using the pytest and Selenium libraries. Additionally, performance tests have been conducted using Locust and JMeter.

## Project Structure

    pythonProject/
    ├── config/
    ├── helpers/
    ├── logs/
    ├── pages/
    ├── performance/
    ├── services/
    ├── test_cases/
    ├── utils/
    ├── requirements.txt


- `config`           : This directory contains constant test data.
- `helpers`          : This directory includes helper classes for API, driver, and UI.
- `logs`             : This directory holds log files generated when tests are executed.
- `pages`            : This directory contains methods specific to pages for UI testing.
- `performance`      : This directory contains files for performance tests written with Locust and JMeter.
- `services`         : This directory includes customized methods for endpoints.
- `test_cases`       : This directory contains API and UI test cases.
- `utils`            : This directory contains utility methods used by other classes.
- `requirements.txt` : This file contains library requirements.

