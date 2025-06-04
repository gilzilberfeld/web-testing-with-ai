## Test Case Suggestions for BStackDemo.com

### I. Login Page - Login Scenarios

**Credentials:**
* **Username:** `demouser`
* **Password:** `testingisfun99`

**Test Cases:**

1.  **Valid Login:**
    * Enter valid username and valid password.
    * Click "Sign In".
    * **Expected:** User is successfully logged in and redirected to the products page. "Products" title is visible.

2.  **Invalid Username:**
    * Enter invalid username (e.g., `invaliduser`).
    * Enter valid password (`testingisfun99`).
    * Click "Sign In".
    * **Expected:** An error message indicating invalid credentials is displayed (e.g., "Invalid Username or Password"). User remains on the login page.

3.  **Invalid Password:**
    * Enter valid username (`demouser`).
    * Enter invalid password (e.g., `wrongpass`).
    * Click "Sign In".
    * **Expected:** An error message indicating invalid credentials is displayed. User remains on the login page.

4.  **Empty Username:**
    * Leave username field empty.
    * Enter valid password (`testingisfun99`).
    * Click "Sign In".
    * **Expected:** An error message (e.g., "Username cannot be empty" or a validation message) is displayed. User remains on the login page.

5.  **Empty Password:**
    * Enter valid username (`demouser`).
    * Leave password field empty.
    * Click "Sign In".
    * **Expected:** An error message (e.g., "Password cannot be empty" or a validation message) is displayed. User remains on the login page.

6.  **Both Fields Empty:**
    * Leave both username and password fields empty.
    * Click "Sign In".
    * **Expected:** Error messages for both empty fields are displayed. User remains on the login page.

7.  **Case Sensitivity (Username):**
    * Enter `Demouser` (different case).
    * Enter valid password.
    * Click "Sign In".
    * **Expected:** (Depends on implementation) Likely invalid login or "Invalid Username or Password".

8.  **Case Sensitivity (Password):**
    * Enter valid username.
    * Enter `Testingisfun99` (different case).
    * Click "Sign In".
    * **Expected:** Likely invalid login or "Invalid Username or Password".

9.  **Tab Key Navigation:**
    * Verify that pressing the Tab key moves focus correctly between username, password, and Sign In button.

10. **Enter Key Submission:**
    * After entering credentials, verify that pressing Enter submits the form.

### II. Product and Cart - All Kinds of Scenarios

**Pre-condition:** User is logged in.

**Test Cases:**

1.  **View Products:**
    * Verify that all products are displayed on the products page.
    * Check for product images, names, and prices.

2.  **Add Single Product to Cart:**
    * Click "Add to cart" for one product.
    * **Expected:** Product is added to the cart. The cart icon (top right) updates with "1" item. A "Checkout" button appears or is enabled.

3.  **Add Multiple Different Products to Cart:**
    * Add 2-3 different products to the cart.
    * **Expected:** The cart icon updates with the correct total number of items. All selected products are listed in the cart when clicked.

4.  **Add Multiple Quantities of the Same Product:**
    * Add the same product multiple times.
    * **Expected:** The quantity of that product in the cart increases accordingly. The cart icon updates with the correct total number of items.

5.  **Remove Product from Cart (from Cart Page):**
    * Add a product to the cart.
    * Click on the cart icon to view the cart details.
    * Click the "Remove" or "Trash" icon next to an item in the cart.
    * **Expected:** The product is removed from the cart. The total number of items in the cart updates.

6.  **Remove All Products from Cart:**
    * Add several products to the cart.
    * Remove all products one by one.
    * **Expected:** The cart becomes empty. The cart icon shows "0" items (or disappears). The "Checkout" button is disabled or disappears.

7.  **Cart Persistency (after navigation/refresh):**
    * Add items to the cart.
    * Navigate to another page (e.g., product details, if available, or just refresh the page).
    * **Expected:** The items remain in the cart.

8.  **Empty Cart Checkout Attempt:**
    * Ensure the cart is empty.
    * Try to click "Checkout" (if the button is visible but disabled).
    * **Expected:** Checkout is not allowed. A message might indicate "Cart is empty."

9.  **Product Details View (if applicable):**
    * Click on a product image or name (if it leads to a detail page).
    * **Expected:** The product detail page opens with more information (description, larger image, etc.). "Add to cart" button is present on this page.

10. **Search Functionality (if available):**
    * Use the search bar (if present) to search for a product by name.
    * **Expected:** Relevant products are displayed in the search results.

11. **Filtering/Sorting (if available):**
    * Test any available filters (e.g., by category, price range) or sorting options (e.g., price low-high, name A-Z).
    * **Expected:** Products are filtered/sorted correctly.

### III. The Whole Ordering Process

**Pre-condition:** User is logged in and has items in the cart.

**Test Cases:**

1.  **Successful Order with Single Item:**
    * Add one product to the cart.
    * Click "Checkout".
    * Fill in valid shipping details (name, address, state, postal code).
    * Select a valid payment method.
    * Click "Place Order".
    * **Expected:** Order is successfully placed. A confirmation message or order confirmation page is displayed with order details. The cart becomes empty.

2.  **Successful Order with Multiple Items:**
    * Add multiple different products to the cart.
    * Click "Checkout".
    * Fill in valid shipping details.
    * Select a valid payment method.
    * Click "Place Order".
    * **Expected:** Order is successfully placed, displaying all ordered items. Cart is emptied.

3.  **Missing Shipping Details - Name:**
    * Add an item to the cart.
    * Proceed to checkout.
    * Leave "First Name" empty.
    * Fill in other valid details.
    * Click "Place Order".
    * **Expected:** Validation error for missing name field. Order is not placed.

4.  **Missing Shipping Details - Address:**
    * Add an item. Proceed to checkout.
    * Leave "Address" empty.
    * Fill in other valid details.
    * Click "Place Order".
    * **Expected:** Validation error for missing address. Order is not placed.

5.  **Missing Shipping Details - State:**
    * Add an item. Proceed to checkout.
    * Leave "State" empty.
    * Fill in other valid details.
    * Click "Place Order".
    * **Expected:** Validation error for missing state. Order is not placed.

6.  **Missing Shipping Details - Postal Code:**
    * Add an item. Proceed to checkout.
    * Leave "Postal Code" empty.
    * Fill in other valid details.
    * Click "Place Order".
    * **Expected:** Validation error for missing postal code. Order is not placed.

7.  **Invalid Shipping Details - Postal Code Format:**
    * Enter an invalid postal code format (e.g., too few digits, letters if only numbers expected).
    * **Expected:** Validation error for incorrect postal code format. Order is not placed.

8.  **Empty Payment Method Selection:**
    * Add an item. Proceed to checkout.
    * Fill in all shipping details.
    * Do not select any payment method (if allowed by UI).
    * Click "Place Order".
    * **Expected:** Validation error for missing payment method. Order is not placed.

9.  **Back Button Functionality during Checkout:**
    * Start the checkout process (e.g., on the shipping details page).
    * Use the browser's back button.
    * **Expected:** User is taken back to the previous page (e.g., cart page) with cart items preserved.

10. **Order History/My Orders (if applicable):**
    * After placing an order, navigate to "My Orders" or "Order History" section (if available).
    * **Expected:** The recently placed order is listed with correct details.

11. **Guest Checkout (if applicable - currently not seen on bstackdemo.com):**
    * (If the site later implements it) Try to checkout as a guest without logging in.
    * **Expected:** User can complete the order as a guest.

12. **Logout after Order:**
    * Place an order.
    * Logout from the application.
    * **Expected:** User is successfully logged out.

13. **Currency Display:**
    * Verify that product prices and total amounts are displayed in the correct currency format (e.g., "$").

14. **Total Price Calculation:**
    * Verify that the total price in the cart and during checkout accurately reflects the sum of all item prices and quantities.

This comprehensive list should help you effectively test bstackdemo.com!