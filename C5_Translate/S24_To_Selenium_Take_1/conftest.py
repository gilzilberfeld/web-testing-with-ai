import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage  # Ensure this import path is correct based on your project structure


@pytest.fixture(scope="function")
def login_page_selenium() -> LoginPage:
    # Set up WebDriver (Chrome in this case)
    # ChromeDriverManager().install() automatically downloads the correct chromedriver binary
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.set_window_size(1920, 1080)  # Set a consistent window size for headless or visual testing

    # Initialize LoginPage object with the Selenium WebDriver instance
    login_page_obj = LoginPage(driver)

    # Navigate to the login page using the Page Object's method
    login_page_obj.navigate()

    # Yield the LoginPage object to the test function
    yield login_page_obj

    # Teardown: close the browser after the test function has completed
    driver.quit()