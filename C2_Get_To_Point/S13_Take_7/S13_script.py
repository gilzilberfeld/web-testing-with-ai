import asyncio
from playwright.async_api import Playwright, async_playwright, expect

async def exploratory_test_add_products(playwright: Playwright) -> None:
    # Launch browser
    browser = await playwright.chromium.launch(headless=False) # Set headless=False to see the browser
    page = await browser.new_page()
    page.set_default_timeout(20000) # Increased default timeout to 20 seconds for robustness

    print("Navigating to login page...")
    await page.goto("https://bstackdemo.com/signin")
    await page.wait_for_load_state('networkidle')

    # --- Locators for login elements ---
    username_field = page.locator('//*[@id="react-select-2-input"]')
    password_field = page.locator('//*[@id="react-select-3-input"]') # Assuming this ID for password
    login_button = page.locator('//button[@id="login-btn"]')

    print("Attempting to fill username...")
    # 1. Click to ensure focus on the React Select component
    await username_field.click()
    # 2. Fill the username
    await username_field.fill("demouser")
    # 3. Assert that the value has been set correctly
    await expect(username_field).to_have_value("demouser", timeout=5000)
    print("Username field filled and verified.")

    print("Attempting to fill password...")
    # 1. Click to ensure focus on the React Select component
    await password_field.click()
    # 2. Fill the password
    await password_field.fill("testingisfun99")
    # 3. Assert that the value has been set correctly
    await expect(password_field).to_have_value("testingisfun99", timeout=5000)
    print("Password field filled and verified.")

    # Press 'Tab' after filling password to dismiss any dropdown/overlay
    print("Pressing Tab to dismiss password dropdown...")
    await password_field.press('Tab')
    await asyncio.sleep(0.3) # Small pause to allow dropdown to fully close

    print("Clicking login button...")
    await login_button.click()

    # Wait for navigation to the products page after successful login
    await page.wait_for_url("https://bstackdemo.com/", timeout=25000) # Increased timeout for navigation
    await page.wait_for_selector(".shelf-container", state="visible", timeout=25000) # Wait for products to load
    print("Successfully logged in and on products page.")

    print("Adding selected iPhone and Galaxy models to cart...")

    async def add_product_to_cart(product_name: str):
        try:
            add_to_cart_button_xpath = f"//div[contains(@class, 'shelf-item') and .//p[text()='{product_name}']]/div[contains(@class, 'shelf-item__footer')]//button[contains(@class, 'buy-btn')]"
            add_to_cart_button = page.locator(add_to_cart_button_xpath)

            await expect(add_to_cart_button).to_be_visible(timeout=10000)
            await expect(add_to_cart_button).to_be_enabled(timeout=10000)

            await add_to_cart_button.click()
            print(f"Added '{product_name}' to cart.")

            await page.wait_for_selector("#cart-count", state="visible")
            await asyncio.sleep(0.5)
        except Exception as e:
            print(f"Could not add '{product_name}' to cart. Error: {e}")
            # await page.screenshot(path=f"error_adding_{product_name.replace(' ', '_')}.png")


    await add_product_to_cart("iPhone 12")
    await add_product_to_cart("iPhone 13")
    await add_product_to_cart("Galaxy S9")
    await add_product_to_cart("Galaxy Note 20")

    print("\nProducts added. You can now perform your exploratory testing.")
    print("The browser will remain open for your manual interaction.")

    await asyncio.Event().wait()

async def main():
    async with async_playwright() as playwright:
        await exploratory_test_add_products(playwright)

if __name__ == "__main__":
    asyncio.run(main())