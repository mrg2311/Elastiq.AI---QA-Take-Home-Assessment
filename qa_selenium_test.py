import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def setup_browser():
    """Setup the browser for Selenium tests."""
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Run in headless mode for faster execution
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    return driver

def test_search_functionality():
    """Test case to validate search functionality on the Selenium Playground website."""
    driver = setup_browser()
    try:
        # Navigate to the target URL
        url = 'https://www.lambdatest.com/selenium-playground/table-sort-search-demo'
        driver.get(url)

        # Locate the search box and search for "New York"
        search_box = driver.find_element(By.XPATH, "//input[@type='search']")
        search_box.send_keys("New York")

        # Validate the search results
        rows = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr")
        visible_rows = [row for row in rows if row.is_displayed()]

        # Assert that there are 5 visible entries
        assert len(visible_rows) == 5, f"Expected 5 entries,found {len(visible_rows)}."


    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    pytest.main(["-v", __file__])
