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
        self.products_main_content = page.get_by_role("main")  # For asserting content on product page

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
