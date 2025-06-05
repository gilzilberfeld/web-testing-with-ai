Sure, that's excellent news that your tests are passing! Refactoring with Pytest fixtures is a smart move; it makes your tests cleaner, more efficient, and easier to maintain by handling setup and teardown automatically.

---

## Refactored Login Tests with Pytest Fixtures

Here are your two login tests refactored to use Pytest fixtures.

### Key Changes:

* **`browser_page_context` fixture:** This fixture handles launching the browser, creating a new context and page, and setting the default timeout. Crucially, it yields the `page` object to the test functions and then automatically closes the context and browser after each test is complete.
* **Test Function Arguments:** The test functions now simply accept `page` as an argument, making them much more concise and focused solely on the test steps.

### How to Run These Tests:

1.  **Save the code:** Save the code below into a Python file (e.g., `test_login_fixtures.py`).
2.  **Install pytest & playwright:** If you haven't already:
    ```bash
    pip install pytest playwright
    playwright install
    ```
3.  **Run from your terminal:**
    ```bash
    pytest test_login_fixtures.py
    ```

```python
import pytest
from playwright.sync_api import Playwright, sync_playwright, Page, expect

# --- Pytest Fixture for Browser, Context, and Page Setup ---
@pytest.fixture(scope="function")
def browser_page_context(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(20000) # Set a default timeout for page actions
    yield page
    context.close()
    browser.close()

# --- Test Cases ---

def test_successful_login(page: Page) -> None:
    page.goto("https://bstackdemo.com/signin")

    page.get_by_text("Select Username").click()
    page.get_by_text("demouser", exact=True).click()

    page.get_by_text("Select Password").click()
    page.get_by_text("testingisfun99", exact=True).click()

    page.get_by_role("button", name="Log In").click()

    expect(page).to_have_url("https://bstackdemo.com/?signin=true", timeout=25000)
    expect(page.get_by_role("main")).to_contain_text("25 Product(s) found.")

def test_invalid_login_no_password(page: Page) -> None:
    page.goto("https://bstackdemo.com/signin")

    page.get_by_text("Select Username").click()
    page.get_by_text("demouser", exact=True).click()

    page.get_by_role("button", name="Log In").click()

    expect(page.get_by_text("Invalid Password")).to_be_visible(timeout=10000)
    expect(page.get_by_text("Invalid Password")).to_have_text("Invalid Password")

    expect(page).to_have_url("https://bstackdemo.com/signin", timeout=5000)
```

---

This refactoring makes your tests cleaner and ensures a consistent testing environment. Do you have more tests you'd like to streamline?