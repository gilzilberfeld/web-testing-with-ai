from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class LoginPage:
    URL = "https://bstackdemo.com/signin"
    DEFAULT_WAIT_TIMEOUT = 20  # seconds

    def __init__(self, driver: WebDriver):
        self.driver = driver

        self.USERNAME_DROPDOWN_TRIGGER = (By.XPATH, "//div[text()='Select Username']")
        self.PASSWORD_DROPDOWN_TRIGGER = (By.XPATH, "//div[text()='Select Password']")
        self.LOGIN_BUTTON = (By.ID, "login-btn")
        # --- FIX START ---
        # More robust XPath for the error message: finds any element that *contains* the text
        self.INVALID_PASSWORD_ERROR = (By.XPATH, "//*[contains(text(), 'Invalid Password')]")
        # --- FIX END ---
        self.PRODUCTS_MAIN_CONTENT = (By.TAG_NAME, "main")

    def navigate(self):
        self.driver.get(self.URL)
        WebDriverWait(self.driver, self.DEFAULT_WAIT_TIMEOUT).until(
            EC.presence_of_element_located(self.USERNAME_DROPDOWN_TRIGGER)
        )

    def _select_dropdown_option(self, dropdown_trigger_locator: tuple, option_text: str):
        WebDriverWait(self.driver, self.DEFAULT_WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(dropdown_trigger_locator)
        ).click()

        option_locator = (By.XPATH, f"//div[text()='{option_text}']")
        option_element = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(option_locator)
        )
        option_element.click()

        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
        time.sleep(0.3)

    def login(self, username: str, password: str):
        self._select_dropdown_option(self.USERNAME_DROPDOWN_TRIGGER, username)
        self._select_dropdown_option(self.PASSWORD_DROPDOWN_TRIGGER, password)

        WebDriverWait(self.driver, self.DEFAULT_WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def login_with_only_username(self, username: str):
        self._select_dropdown_option(self.USERNAME_DROPDOWN_TRIGGER, username)

        WebDriverWait(self.driver, self.DEFAULT_WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def get_driver(self) -> WebDriver:
        return self.driver

    def get_invalid_password_error_element(self):
        # This will now use the more flexible XPath
        return WebDriverWait(self.driver, self.DEFAULT_WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(self.INVALID_PASSWORD_ERROR)
        )

    def get_products_main_content_element(self):
        return WebDriverWait(self.driver, self.DEFAULT_WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(self.PRODUCTS_MAIN_CONTENT)
        )