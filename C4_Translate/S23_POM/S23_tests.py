import pytest
from playwright.sync_api import Playwright, expect, Page, Locator
from login_page import LoginPage  # Import the LoginPage class


# --- Pytest Fixture for LoginPage Object Setup ---
@pytest.fixture(scope="function")
def login_page(playwright: Playwright) -> LoginPage:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(20000)  # Set a default timeout for page actions

    # Initialize LoginPage object
    login_page_obj = LoginPage(page)

    # Navigate to the login page using the Page Object's method
    login_page_obj.navigate()

    yield login_page_obj  # Yield the LoginPage object to the test function

    # Teardown: close context and browser after the test
    context.close()
    browser.close()


# --- Test Cases ---

def test_successful_login(login_page: LoginPage) -> None:
    # Perform login using the Page Object's method
    login_page.login("demouser", "testingisfun99")

    # Assertions using the Page Object's methods/properties
    expect(login_page.get_page()).to_have_url("https://bstackdemo.com/?signin=true", timeout=25000)
    expect(login_page.get_products_main_content_locator()).to_contain_text("25 Product(s) found.")


def test_invalid_login_no_password(login_page: LoginPage) -> None:
    # Perform invalid login using the Page Object's method
    login_page.login_with_only_username("demouser")

    # Assertions using the Page Object's methods/properties
    error_message_locator = login_page.get_invalid_password_error_locator()
    expect(error_message_locator).to_be_visible(timeout=10000)
    expect(error_message_locator).to_have_text("Invalid Password")

    expect(login_page.get_page()).to_have_url(login_page.URL, timeout=5000)  # Use the URL constant from the Page Object