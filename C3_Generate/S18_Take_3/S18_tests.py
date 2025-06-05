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

    # Intentionally skip selecting a password to trigger an invalid login
    page.get_by_role("button", name="Log In").click()

    expect(page.get_by_text("Invalid Username or Password")).to_be_visible(timeout=10000)
    expect(page.get_by_text("Invalid Username or Password")).to_have_text("Invalid Username or Password")

    expect(page).to_have_url("https://bstackdemo.com/signin", timeout=5000)

    context.close()
    browser.close()