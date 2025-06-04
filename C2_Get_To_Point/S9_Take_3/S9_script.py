import asyncio
from playwright.async_api import Playwright, async_playwright, expect


async def exploratory_test_add_products(playwright: Playwright) -> None:
    # Launch browser
    browser = await playwright.chromium.launch(headless=False)  # Set headless=False to see the browser
    page = await browser.new_page()
    page.set_default_timeout(15000)  # Increased default timeout slightly to 15 seconds

    print("Navigating to login page...")
    await page.goto("https://bstackdemo.com/signin")

    # --- Added explicit wait for the login form elements to be present ---
    # This ensures the main login form is loaded before attempting to fill fields
    await page.wait_for_selector("//form[@id='login-form']", state="visible", timeout=20000)
    print("Login form is visible. Proceeding to login...")

    # Using XPath for username and password fields
    username_field = page.locator("//input[@name='username']")
    password_field = page.locator("//input[@name='password']")
    login_button = page.locator("//button[@id='login-btn']")  # Using XPath for the button

    print("Logging in...")
    await username_field.fill("demouser")
    await password_field.fill("testingisfun99")

    await login_button.click()

    # Wait for navigation to the products page after successful login
    await page.wait_for_url("https://bstackdemo.com/", timeout=20000)  # Increased timeout for navigation
    await page.wait_for_selector(".shelf-container", state="visible", timeout=20000)  # Wait for products to load
    print("Successfully logged in and on products page.")

    print("Adding selected iPhone and Galaxy models to cart...")

    # Function to add a product to cart by its name using a more robust XPath
    async def add_product_to_cart(product_name: str):
        try:
            # This XPath locates the 'Add to cart' button directly within the shelf-item
            # that contains the product name as its text.
            add_to_cart_button_xpath = f"//div[contains(@class, 'shelf-item') and .//p[text()='{product_name}']]/div[contains(@class, 'shelf-item__footer')]//button[contains(@class, 'buy-btn')]"
            add_to_cart_button = page.locator(add_to_cart_button_xpath)

            # Ensure the button is visible and enabled before clicking
            await expect(add_to_cart_button).to_be_visible(timeout=10000)
            await expect(add_to_cart_button).to_be_enabled(timeout=10000)

            await add_to_cart_button.click()
            print(f"Added '{product_name}' to cart.")

            # Wait for the cart count to update (cart icon usually changes)
            await page.wait_for_selector("#cart-count", state="visible")
            await asyncio.sleep(0.5)  # Small pause for visual confirmation
        except Exception as e:
            print(f"Could not add '{product_name}' to cart. Error: {e}")
            # Optional: take a screenshot if a product fails to add
            # await page.screenshot(path=f"error_{product_name.replace(' ', '_')}.png")

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