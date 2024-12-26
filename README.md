# Elastiq.AI---QA-Take-Home-Assessment
README/Documentation

Overview

This Python script automates the testing of the search functionality on the Selenium Playground website. The script navigates to the "Table Sort and Search Demo" page, performs a search for "New York," and validates that the displayed results meet the expected criteria.

Functionality

Navigates to the page: https://www.lambdatest.com/selenium-playground/table-sort-search-demo.

Interacts with the search box to input "New York."

Validates:

The number of visible entries matches the expected result (5 entries).

The total number of entries on the page (24 total entries).

Best Practices Followed

Modular Design: The browser setup is encapsulated in a separate function for reusability.

Robust Assertions: Assertions include meaningful error messages to facilitate debugging.

Headless Execution: The script uses headless mode for efficiency, which is ideal for CI/CD pipelines.

PEP 8 Compliance: The code adheres to Python’s style guide for readability and maintainability.

Resource Management: The finally block ensures the browser closes properly, even in case of test failure.

Dependency Management: webdriver_manager handles ChromeDriver installation, removing manual setup steps.

Prerequisites

Python 3.8 or later

Google Chrome (latest version)

Required Python packages:

selenium

pytest

webdriver-manager

Setup Instructions

Clone the repository or save the script to your local machine.

Install the necessary dependencies:

pip install selenium pytest webdriver-manager

How to Run the Script

Save the script as qa_selenium_test.py.

Run the script using pytest:

pytest qa_selenium_test.py

Validation Steps

The script performs the following checks:

Ensures 5 entries are displayed in the search results after searching for "New York."

Verifies that the total entries count on the page is "24 total entries" as indicated by the footer text.

Customizations

Modify the search term by changing the input string in the search_box.send_keys("New York") line.

Add additional assertions or validations as needed for further testing scenarios.

Troubleshooting

Common Errors:

AssertionError: Indicates a mismatch between expected and actual results. Verify the website's structure or update the expected text to align with changes in the page content.

NoSuchElementException: Ensure that the page is fully loaded, and the selectors used are correct.

Debugging: Run the script in non-headless mode by commenting out options.add_argument('--headless') to visually inspect browser behavior.

Future Improvements

Add compatibility for additional browsers like Firefox.

Integrate with CI/CD tools for automated testing.

Parameterize the search term and expected results for increased flexibility.

