import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import the fixture and LoginPage class
from login_page import LoginPage
# from conftest import login_page_selenium # You typically don't need to import the fixture directly if conftest.py is discoverable

def test_successful_login_selenium(login_page_selenium: LoginPage) -> None:
    # Perform login using the Page Object's method
    login_page_selenium.login("demouser", "testingisfun99")

    # Assertions for successful login
    # Check URL
    WebDriverWait(login_page_selenium.get_driver(), 25).until(
        EC.url_to_be("https://bstackdemo.com/?signin=true")
    )
    # Check content on the product page
    products_main_content_element = login_page_selenium.get_products_main_content_element()
    assert "25 Product(s) found." in products_main_content_element.text

def test_invalid_login_no_password_selenium(login_page_selenium: LoginPage) -> None:
    # Perform invalid login using the Page Object's method
    login_page_selenium.login_with_only_username("demouser")

    # Assertions for invalid login
    error_message_element = login_page_selenium.get_invalid_password_error_element()
    assert error_message_element.is_displayed()
    assert error_message_element.text == "Invalid Password"

    # Check URL remains the login page
    WebDriverWait(login_page_selenium.get_driver(), 5).until(
        EC.url_to_be(login_page_selenium.URL)
    )