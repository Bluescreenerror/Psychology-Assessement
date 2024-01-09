
# Psychological Assessment Tool
## Description
This Python-based Psychological Assessment Tool is a digital adaptation of three psychology tests designed for high school students. It brings the realms of psychology and programming together, offering an innovative approach to assess various psychological aspects such as anxiety, personality, and self-concept. The tool digitizes traditional paper-based tests, making them more accessible and efficient.

## Features
Three Tests in One: Includes the Adjustment Inventory for School Students (AISS), Self-Concept Questionnaire (SCQ), and Sinha's Comprehensive Anxiety Test (SCAT).
Interactive Interface: Utilizes libraries like PyInquirer and colorama for a user-friendly interactive command-line interface.
Database Integration: Incorporates MySQL for storing and retrieving test results.
Real-time Analysis and Feedback: Provides instant analysis and categorization based on the responses.
Flagging System: Identifies students who may need further attention based on their test results.
##Requirements
Python 3
Libraries: colorama, mysql-connector-python, PyInquirer, rich, pyfiglet
MySQL Database
## Installation
1. Ensure Python 3 and MySQL are installed on your system.
2. Install the required Python libraries using pip:
```pip install colorama mysql-connector-python PyInquirer rich pyfiglet```
4. Set up a MySQL database named psychology with the required tables (refer to the script for table schemas).
## Usage
1. Run the script using Python.
2. Follow the on-screen instructions to choose and complete the tests.
3. Access the results from the database for analysis and further actions.
## How It Works
1. Test Selection: Users select the test they wish to take - AISS, SCQ, or SCAT.
2. Interactive Questions: The test is presented in a question-and-answer format.
3. Real-time Analysis: Upon completion, the tool analyzes the answers and displays the results.
4. Database Logging: The results are logged into the MySQL database for record-keeping and analysis.
5. Flagging System: Identifies and flags students needing additional support or attention.
## Note
The tool is intended for educational and informational purposes.
Ensure proper ethical guidelines and privacy measures are followed while using this tool.
## Disclaimer
This tool is not a substitute for professional psychological advice, diagnosis, or treatment. Always seek the advice of qualified health providers with any questions you may have regarding a medical condition.
