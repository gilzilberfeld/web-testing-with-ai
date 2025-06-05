The test below works. It finds the locators, and operates the text boxes with no problems.
Rewrite the tests I asked you, to work in the same way, based on this test.

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
    expect(page.get_by_role("main")).to_contain_text("25 Product(s) found.")

    # ---------------------
    context.close()
    browser.close()

