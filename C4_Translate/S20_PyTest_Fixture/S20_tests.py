import pytest
from playwright.sync_api import Playwright, sync_playwright, Page, expect


# --- Pytest Fixture for Browser, Context, and Page Setup ---
@pytest.fixture(scope="function")
def browser_page_context(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(20000)  # Set a default timeout for page actions
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
