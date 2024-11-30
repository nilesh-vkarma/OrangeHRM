**WebUI Automation Framework**

This repository contains a robust WebUI Automation Framework designed for end-to-end testing of web applications. The framework is built using Python, Selenium, and Pytest, following modern best practices like the Page Object Model (POM), fixtures for modular test design, and sensitive data protection using a config.properties file.

**Key Features**

* Python-Based: Developed entirely in Python for ease of use and scalability.
* Selenium Integration: Utilizes Selenium WebDriver for browser-based automation.
* Pytest Framework: Leverages Pytest for test execution, parameterization, and reporting.
* Page Object Model (POM): Implements POM for reusability, maintainability and reusability of code.
* Data-Driven Testing: Uses OpenPYXL for reading test data from Excel files. alo for generating simple readable reports of automation testing.
* Fixtures: Implements Pytest fixtures for modular, reusable test setup and teardown.
* Sensitive Data Protection: Manages sensitive data (e.g., credentials, environment URLs) through a config.properties file to ensure security and easy environment management.
* Cross-Browser Testing Ready: Supports testing across multiple browsers (Chrome, Firefox, etc.).


**Guide to Setup the automation framework**

Step 1: Set Up Your Environment
1. Install Python
Download and Install Python: Go to the official Python website and download the latest version. Make sure to check the box that says "Add Python to PATH" during installation.
2. Install PyCharm
Download and Install PyCharm: Go to the JetBrains website and download the Community Edition (free). Install it on your computer.
3. Create a New Project in PyCharm
* Open PyCharm.
* Click on "New Project"
* Choose a location for your project and name it (e.g., WebUIframework).
* Ensure the interpreter is set to the Python version you installed.
* Click "Create."

Step 2: Install Required Packages
1. Open Terminal in PyCharm
2. Install Selenium
Run the following command in the terminal: pip install selenium
3. Install WebDriver
Download WebDriver: Depending on the browser you want to automate (e.g., Chrome, Firefox), download the corresponding WebDriver:

ChromeDriver: [ChromeDriver Download](https://sites.google.com/chromium.org/driver/)
GeckoDriver (Firefox): [GeckoDriver Download](https://github.com/mozilla/geckodriver/releases)
Add WebDriver to PATH: Extract the downloaded WebDriver and place it in a directory that is included in your system's PATH, or specify its location in your scripts.
