You are absolutely right. Thanks for the correction!

Here are the updated tests with the correct error message for the invalid login scenario.

---

### Login Screen Tests

```python
from playwright.sync_api import Playwright, sync_playwright, expect

def test_successful_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://bstackdemo.com/signin")

    page.get_by_text("Select Username").click()
    page.get_by_text("demouser", exact=True).click()

    page.get_by_text("Select Password").click()
    page.get_by_text("testingisfun99", exact=True).click()

    page.get_by_role("button", name="Log In").click()

    expect(page).to_have_url("https://bstackdemo.com/?signin=true", timeout=25000)
    expect(page.get_by_role("main")).to_contain_text("25 Product(s) found.")

    context.close()
    browser.close()

def test_invalid_login_no_password(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://bstackdemo.com/signin")

    page.get_by_text("Select Username").click()
    page.get_by_text("demouser", exact=True).click()

    page.get_by_role("button", name="Log In").click()

    expect(page.get_by_text("Invalid Password")).to_be_visible(timeout=10000)
    expect(page.get_by_text("Invalid Password")).to_have_text("Invalid Password")

    expect(page).to_have_url("https://bstackdemo.com/signin", timeout=5000)

    context.close()
    browser.close()
```