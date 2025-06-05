Applying the Page Object Model (POM) pattern will significantly improve the maintainability and readability of your tests. Each web page (or distinct part of it) gets its own class, centralizing its locators and interactions.

Here's how to refactor your tests using POM:

---

### Step 1: Create the Page Object Class (`pages/login_page.py`)

First, create a new directory (e.g., `pages`) and a Python file inside it named `login_page.py`. This file will contain your `LoginPage` class.

**`pages/login_page.py`**
```python
from playwright.sync_api import Page, Locator

class LoginPage:
    URL = "https://bstackdemo.com/signin"

    def __init__(self, page: Page):
        self.page = page
        # Define locators as instance attributes
        self.username_dropdown_trigger = page.get_by_text("Select Username")
        self.username_option_demouser = page.get_by_text("demouser", exact=True)
        self.password_dropdown_trigger = page.get_by_text("Select Password")
        self.password_option_testingisfun99 = page.get_by_text("testingisfun99", exact=True)
        self.login_button = page.get_by_role("button", name="Log In")
        self.invalid_password_error = page.get_by_text("Invalid Password")
        self.products_main_content = page.get_by_role("main") # For asserting content on product page

    def navigate(self):
        """Navigates to the login page."""
        self.page.goto(self.URL)
        self.page.wait_for_load_state('networkidle')

    def login(self, username: str, password: str):
        """Performs a full login sequence."""
        self.username_dropdown_trigger.click()
        self.page.get_by_text(username, exact=True).click()

        self.password_dropdown_trigger.click()
        self.page.get_by_text(password, exact=True).click()

        self.login_button.click()

    def login_with_only_username(self, username: str):
        """Performs login attempt by selecting username but not password."""
        self.username_dropdown_trigger.click()
        self.page.get_by_text(username, exact=True).click()
        self.login_button.click()

    # --- Methods to return locators for assertions in tests (if needed) ---
    def get_page(self) -> Page:
        return self.page

    def get_invalid_password_error_locator(self) -> Locator:
        return self.invalid_password_error

    def get_products_main_content_locator(self) -> Locator:
        return self.products_main_content
```

### Step 2: Modify Your Test File (`tests/test_login.py`)

Next, modify your test file to import and use the `LoginPage` class within your fixture and test functions.

**`tests/test_login.py`**
```python
import pytest
from playwright.sync_api import Playwright, expect, Page, Locator
from pages.login_page import LoginPage # Import the LoginPage class

# --- Pytest Fixture for LoginPage Object Setup ---
@pytest.fixture(scope="function")
def login_page(playwright: Playwright) -> LoginPage:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(20000) # Set a default timeout for page actions
    
    # Initialize LoginPage object
    login_page_obj = LoginPage(page)
    
    # Navigate to the login page using the Page Object's method
    login_page_obj.navigate() 

    yield login_page_obj # Yield the LoginPage object to the test function
    
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

    expect(login_page.get_page()).to_have_url(login_page.URL, timeout=5000) # Use the URL constant from the Page Object
```

---

### How to Run:

1.  **Project Structure:** Make sure your files are organized like this:
    ```
    your_project_root/
    ├── pages/
    │   └── login_page.py
    └── tests/
        └── test_login.py
    ```
2.  **Run Pytest:** Open your terminal in `your_project_root/` and run:
    ```bash
    pytest tests/test_login.py
    ```

This refactoring centralizes your locators and interactions within the `LoginPage` class, making your tests more readable, resilient to UI changes, and easier to scale as your test suite grows.