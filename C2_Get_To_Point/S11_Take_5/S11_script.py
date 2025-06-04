import asyncio
from playwright.async_api import Playwright, async_playwright, expect


async def exploratory_test_add_products(playwright: Playwright) -> None:
    # Launch browser
    browser = await playwright.chromium.launch(headless=False)  # Set headless=False to see the browser
    page = await browser.new_page()
    page.set_default_timeout(15000)  # Increased default timeout slightly to 15 seconds

    print("Navigating to login page...")
    await page.goto("https://bstackdemo.com/signin")
    # Wait for the page to be fully loaded, which should include the React Select inputs
    await page.wait_for_load_state('networkidle')

    # --- UPDATED LOCATORS BASED ON YOUR PROVIDED XPATH ---
    # Username field using the exact ID you provided
    username_field = page.locator('//*[@id="react-select-2-input"]')

    # Educated guess for the password field's ID (common React Select pattern)
    # If this still times out, you might need to inspect the password field's ID in your browser.
    password_field = page.locator('//*[@id="react-select-3-input"]')

    # Login button - confirmed as a real button element with this ID
    login_button = page.locator('//button[@id="login-btn"]')

    print("Logging in...")
    # Playwright's .fill() automatically waits for the element to be visible, enabled, and editable
    await username_field.fill("demouser")
    await password_field.fill("testingisfun99")

    await login_button.click()

    # Wait for navigation to the products page after successful login
    await page.wait_for_url("https://bstackdemo.com/", timeout=20000)
    await page.wait_for_selector(".shelf-container", state="visible", timeout=20000)  # Wait for products to load
    print("Successfully logged in and on products page.")

    print("Adding selected iPhone and Galaxy models to cart...")

    # Function to add a product to cart by its name using a robust XPath
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
            # Optional: take a screenshot if a product fails to add
            # await page.screenshot(path=f"error_adding_{product_name.replace(' ', '_')}.png")

    # Add specific iPhone models
    await add_product_to_cart("iPhone 12")
    await add_product_to_cart("iPhone 13")

    # Add specific Galaxy models
    await add_product_to_cart("Galaxy S9")
    await add_product_to_cart("Galaxy Note 20")

    print("\nProducts added. You can now perform your exploratory testing.")
    print("The browser will remain open for your manual interaction.")

    # To keep the browser open indefinitely for manual exploration:
    await asyncio.Event().wait()

    # If you prefer to close it after a certain time (e.g., 5 minutes):
    # await asyncio.sleep(300) # Keep browser open for 5 minutes
    # await browser.close()


async def main():
    async with async_playwright() as playwright:
        await exploratory_test_add_products(playwright)


if __name__ == "__main__":
    asyncio.run(main())