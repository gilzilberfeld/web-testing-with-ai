from playwright.sync_api import Playwright, sync_playwright, expect

def test_successful_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_default_timeout(20000)

    page.goto("https://bstackdemo.com/signin")
    page.wait_for_load_state('networkidle')

    username_input = page.get_by_role("combobox", name="Username")
    password_input = page.get_by_role("combobox", name="Password")
    login_button = page.get_by_role("button", name="Sign In")

    username_input.click()
    username_input.fill("demouser")
    expect(username_input).to_have_value("demouser", timeout=5000)

    password_input.click()
    password_input.fill("testingisfun99")
    expect(password_input).to_have_value("testingisfun99", timeout=5000)

    page.keyboard.press('Tab')

    login_button.click()

    expect(page).to_have_url("https://bstackdemo.com/", timeout=25000)
    expect(page.locator(".shelf-container")).to_be_visible(timeout=25000)

    browser.close()

def test_invalid_login_wrong_user(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_default_timeout(20000)

    page.goto("https://bstackdemo.com/signin")
    page.wait_for_load_state('networkidle')

    username_input = page.get_by_role("combobox", name="Username")
    password_input = page.get_by_role("combobox", name="Password")
    login_button = page.get_by_role("button", name="Sign In")

    username_input.click()
    username_input.fill("wronguser")
    expect(username_input).to_have_value("wronguser", timeout=5000)

    password_input.click()
    password_input.fill("testingisfun99")
    expect(password_input).to_have_value("testingisfun99", timeout=5000)

    page.keyboard.press('Tab')

    login_button.click()

    error_message_locator = page.get_by_text("Invalid Username or Password")
    expect(error_message_locator).to_be_visible(timeout=10000)
    expect(error_message_locator).to_have_text("Invalid Username or Password")

    expect(page).to_have_url("https://bstackdemo.com/signin", timeout=5000)

    browser.close()

# To run these tests:
# 1. Save this code as a Python file (e.g., `login_tests.py`).
# 2. Make sure you have Playwright and pytest installed: `pip install pytest playwright`.
# 3. Install browser binaries: `playwright install`.
# 4. Run from your terminal: `pytest login_tests.py`

# Optional: You can also run them directly using a main block:
if __name__ == "__main__":
    with sync_playwright() as p:
        try:
            test_successful_login(p)
            print("Successful login test passed!")
        except Exception as e:
            print(f"Successful login test failed: {e}")

    with sync_playwright() as p:
        try:
            test_invalid_login_wrong_user(p)
            print("Invalid login test (wrong user) passed!")
        except Exception as e:
            print(f"Invalid login test (wrong user) failed: {e}")