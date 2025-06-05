from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  # For pressing Tab key


class LoginPage:
    URL = "https://bstackdemo.com/signin"
    # Define a default timeout for explicit waits in the Page Object
    DEFAULT_WAIT_TIMEOUT = 20  # seconds

    def __init__(self, driver: WebDriver):
        self.driver = driver

        # Define locators as instance attributes using Selenium's By strategy
        self.USERNAME_DROPDOWN_TRIGGER = (By.XPATH, "//div[text()='Select Username']")
        self.PASSWORD_DROPDOWN_TRIGGER = (By.XPATH, "//div[text()='Select Password']")
        self.LOGIN_BUTTON = (By.ID, "login-btn")  # Using ID as it's more stable if available
        self.INVALID_PASSWORD_ERROR = (By.XPATH, "//div[text()='Invalid Password']")
        self.PRODUCTS_MAIN_CONTENT = (By.TAG_NAME, "main")  # For asserting content on product page

    def navigate(self):
        """Navigates to the login page and waits for it to load."""
        self.driver.get(self.URL)
        # Wait for the username dropdown to be present as an indicator of page load
        WebDriverWait(self.driver, self.DEFAULT_WAIT_TIMEOUT).until(
            EC.presence_of_element_located(self.USERNAME_DROPDOWN_TRIGGER)
        )

    def _select_dropdown_option(self, dropdown_trigger_locator: tuple, option_text: str):
        """Helper method to interact with the react-select dropdowns."""
        # 1. Click the visible dropdown trigger to open the options
        WebDriverWait(self.driver, self.DEFAULT_WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(dropdown_trigger_locator)
        ).click()

        # 2. Locate and click the specific option by its text within the opened dropdown
        option_locator = (By.XPATH, f"//div[text()='{option_text}']")
        option_element = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(option_locator)
        )
        option_element.click()

        # 3. Send TAB key to close the dropdown and move focus away (prevents interception)
        # We send it to the body or the element itself, depends on what closes it.
        # Sending to the selected option is a good robust choice.
        option_element.send_keys(Keys.TAB)

    def login(self, username: str, password: str):
        """Performs a full login sequence."""
        self._select_dropdown_option(self.USERNAME_DROPDOWN_TRIGGER, username)
        self._select_dropdown_option(self.PASSWORD_DROPDOWN_TRIGGER, password)

        # Click the login button
        WebDriverWait(self.driver, self.DEFAULT_WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def login_with_only_username(self, username: str):
        """Performs login attempt by selecting username but not password."""
        self._select_dropdown_option(self.USERNAME_DROPDOWN_TRIGGER, username)

        # Click the login button without selecting password
        WebDriverWait(self.driver, self.DEFAULT_WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    # --- Methods to return elements or check page state for assertions in tests ---
    def get_driver(self) -> WebDriver:
        return self.driver

    def get_invalid_password_error_element(self):
        """Returns the web element for the 'Invalid Password' error message."""
        return WebDriverWait(self.driver, self.DEFAULT_WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(self.INVALID_PASSWORD_ERROR)
        )

    def get_products_main_content_element(self):
        """Returns the web element for the main content on the products page."""
        return WebDriverWait(self.driver, self.DEFAULT_WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(self.PRODUCTS_MAIN_CONTENT)
        )