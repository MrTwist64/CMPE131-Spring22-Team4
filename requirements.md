## Functional Requirements

### High Priority

1. :heavy_check_mark: Login - Nhan
2. :heavy_check_mark: Logout - Nhan
3. :heavy_check_mark: Create New Account - Nhan
4. :heavy_check_mark: Delete Account - Nhan
5. :heavy_check_mark: Update Account - Nhan
6. :heavy_check_mark: Forgot Password - Nhan
7. :heavy_check_mark: Seller Create Item - Aaron
8. :x: Seller Update Item - Aaron
9. :heavy_check_mark: Seller Delete Item - Aaron
10. :heavy_check_mark: View Available Items - Aaron
11. :heavy_check_mark: View Single Item - Aaron
12. :x: Add Item to Cart - Anh
13. :x: View Current Cart - Aaron
14. :x: Remove Item From Cart - Anh
15. :x: Buy Items From Cart - Anh
16. :x: Maintain UI Consistency - Nhan
17. :x: (HP) Add Pictures To Items - TBD

### Medium Priority
17. :heavy_check_mark: (HP) Add Item Categories
18. :x: Purchase History Database
19. :x: View Purchase History
20. :x: Picture Database

### Low Priority
- Add Discount Codes
- Seller Item List Page
- Seller Update Item
- Item Search Functionality
- Sort Items
- Seller and Item Reviews
- Cancel Ordered Item
- "Feeling Lucky?" Button (Suggests random item)
- Website Splash Page
- Recently Viewed Items
- Google Calender API for Discount Code Expiry Date
- Seller Announcements
- Google Analytics API for Seller to View Buyer Demographics
- Save for Later
- Seller Dashboard
- Social Media Integration
- Item Quantities
- User Verification With Email

## Non-functional Requirements

1. Expected to work on Google Chrome
2. Multilingual Support with Google Translate?
3. (HP) UI Interactive Interface
4. Attempt to be seccure:
  a. Lock out user after multiple failed login attempts
  b. Prevent basic SQL injection
5. Accessibility function (dark mode)

## Use Cases

### 1. Add Item to Cart - Nhan
- **Summary:** The user can add an item to their shopping cart.
- **Actors:** User
- **Pre-Condition:** 
  - The user is logged into their account.
  - The user is viewing an item.
  - The item is available for purchase.
- **Trigger:** The user clicks "Add to Cart" from an item page.
- **Primary Sequence:** 
  1. The cart is updated with the product added to the total.
  2. The user's subtotal is updated according to the item price.
- **Alternative Sequence:** The item is not available.
  1. The system shows the user that the item is not available to add to cart.
- **Alternative Sequence:** The item already exists in the cart.
  1. The system notifies the user that the item has already been added to the cart.
- **Post Conditions:**
  - The item is available and is not already in the cart:
    - The user's cart is updated with the item.
- **Functional Requirements:**
  - The system can check how many items the user has in their cart.
  - The system can update the user's cart.
  - The system can update the user's subtotal.
- **Non-Functional Requirements:**
  - The website is stylized.
- **Glossary:**
  - Item = A product that is sold on the website.
  - User = Customer who wants to buy one or more items.
  - Cart = A list of items the user would like to buy.

### 2. Remove item from cart - Nhan
- **Summary:** The user can remove an item from the cart.
- **Actors:** User
- **Pre-Condition:** 
  - The user is logged into their account.
  - The user is viewing their cart.
  - The user has at least 1 item in the cart.
- **Trigger:** The user clicks “Remove from cart” from the cart.
- **Primary Sequence:** 
  1. The item is removed from the cart.
  2. The user’s subtotal is updated according to the product price.
- **Alternative Sequence:** The item(s) are no longer in the cart.
  1. The system informs the user that the item no longer exists in the cart.
- **Post Conditions:**
  - The item is has a quantity greater than 1:
    - The user’s cart is updated.
    - The user’s subtotal is updated.
  - The item no longer exist in the cart:
    - The user is informed that the item no longer exists.
    - The page refreshes.
- **Functional Requirements:**
  - The system can check how many items the user has in their cart
  - The system can update the user’s cart
  - The system can update the user’s subtotal
- **Non-Functional Requirements:**
  - The website is stylized.
- **Glossary:**
  - Item = A product that is sold on the website.
  - User = Customer who wants to buy one or more items.
  - Cart = A list of items the user would like to buy.

### 3. Buy items from cart - Aaron
- **Summary:** A user can buy the items in their cart.
- **Actors:** User
- **Pre-Condition:** 
  - The user is logged into their account.
  - The user has items in their cart.
  - The user is currently on their cart page.
- **Trigger:** The user clicks “Buy Cart” from their cart page.
- **Primary Sequence:** 
  1. The system shows the user their subtotal.
  2. The system shows a payment method using an outside payment platform.
  3. The user selects their desired payment method using the outside platform.
  4. The user clicks “Buy”.
  5. The system checks the items availability.
  6. The system charges the payment method.
  7. The system marks the items as purchased.
  8. The system shows the user that the items have been purchased.
  9. The system adds the items to the user’s purchase history.
- **Alternative Sequence:** The item(s) are not available.
  1. The system shows the user the item(s) that is not available.
  2. The user must remove the items that are unavailable.
  3. Continue to Step 4 in Primary Sequence.
- **Alternative Sequence:** The payment method cannot be charged.
  1. The system tells the user that the payment method could not be charged.
  2. The user selects a new payment method.
  3. Continue to Step 4 in Primary Sequence.
- **Alternative Sequence:** The user clicks “Cancel Purchase
  1. The user is sent back to the cart page.
- **Post Conditions:**
  - The items were bought:
    - The item(s) sold are made unavailable to be sold again
    - The quantity of the item decreases on bulk items.
    - The items are sent to the user.
  - The items were not bought:
    - The item(s) are not changed.
- **Functional Requirements:**
  - The system can check whether items are available.
  - The system can check whether a payment has gone through.
  - The system can make purchased items unavailable.
- **Non-Functional Requirements:**
  - The website is stylized.
- **Glossary:**
  - Item = A product that is sold on the website.
  - User = Customer who wants to buy one or more items.
  - Cart = A list of items the user would like to buy.

### 4. Seller Creates Item - Anh
- **Summary:** A user can create an item to sell.
- **Actors:** User
- **Pre-Condition:** 
  - The user is logged into their account.
  - The user has an item they intend to sell.
  - The user knows basic information and description of the item.
  - The system allows any user to buy and sell.
- **Trigger:** The user clicks on “sell an item”.
- **Primary Sequence:** 
  1. The user adds the product name.
  2. The user selects item condition (new, used).
  3. The user selects item categories and tags.
  4. The user adds an item description about the product.
  5. The user selects the quantity of the item to sell.
  6. The user includes the price of the item.
  7. The system prompts the user to upload photos of the item.
  8. The user uploads item photos.
  9. The user clicks “post to listing”.
  10. The system adds the item to the database of the items to be sold.
- **Alternative Sequence:** The user does not fill in all the required information of the item (product name, condition, categories, description, and price)
  1. The system will cause an error and display the item has not been added yet.
  2. The system displays which item information is blank.
  3. The system prompts the user to add missing required information.
  4. When the user adds in the information of the item, the system will allow the user to add the item into the sell items database.
- **Alternative Sequence:** The user does not upload any item photos.
  1. The system uploads a placeholder photo.
  2. The system adds the item to the items database.
- **Alternative Sequence:** The user does not add an item to sell.
  1. The system would cause an error due to missing item information.
  2. The user clicks the back button.
  3. The item is not added to the sell items database and is not listed in the store.
- **Alternative Sequence:** The user is not logged in.
  1. The system redirects the user to the login page.
- **Post Conditions:**
  - The user listed an item to sell.
    - The items are displayed on the page to the user as products in their seller inventory.
    - The items are displayed on the page to other users who did not list that particular product as items they can buy.
  - The user did not list an item to sell.
    - The seller inventory page remains the same.
    - The items listing page remains the same.
- **Functional Requirements:**
  - The system has access to the user and items databases.
  - The system creates an item to sell.
- **Non-Functional Requirements:**
  - The website is stylized and consistent.
- **Glossary:**
  - Required information of the item = product name, condition, categories, description, and price
  - Item to sell = A product that the user wants to sell.
  - User = Customer who wants to sell one or more items.

### 5. Seller Deletes Item - Haomiao
- **Summary:** A user can select an item to delete.
- **Actors:** User
- **Pre-Condition:** 
  - The user is logged into their account.
  - The user has an item they intend to delete.
  - The user knows basic information and description of the item.
  - The system allows any user to delete.
- **Trigger:** The user clicks on “delete an item”.
- **Primary Sequence:** 
  1. The user adds the product name.
  2. The user selects item.
  3. The user selects the quantity of the item to delete.
  4. The user includes the price of the item.
  5. The user clicks “delete”.
  6. The system adds the item to the database of the items to be deleted.
- **Alternative Sequence:** The user does not select the item.
  1. The system will cause an error and display the item has not been selected yet.
  2. The system displays which item information is blank.
  3. The system prompts the user to select.
  4. When the user select the item, the system will allow the user to add the item into the delete items database.
- **Alternative Sequence:** The user is not logged in.
  1. The system redirects the user to the login page.
- **Post Conditions:**
  - The user listed an item to delete.
    - The items are displayed on the page to the user as products in their delete inventory.
    - The items are displayed on the page to other users that the items are deleted.
- **Functional Requirements:**
  - The system has access to the user and items databases.
  - The system creates an item to delete.
- **Non-Functional Requirements:**
  - The website is stylized.
- **Glossary:**
  - required information of the item = product name, condition, categories, description, and price
  - Item to delete= A product that the user wants to sell.
  - User = Customer who wants to delete one or more items.

### 6. View Purchase History - Aaron
- **Summary:** A user can view all purchased items
- **Actors:** User
- **Pre-Condition:** 
  - The user is logged into their account.
- **Trigger:** The user visits the purchase history page.
- **Primary Sequence:** 
  1. The system searches for purchases tied to the user.
  2. The system displays each purchase sequentially on the page.
  3. The user can click on the item of a purchase to be brought to its item page.
- **Alternative Sequence:** The user does not have any purchases.
  1. The system displays that no purchases could be found.
- **Alternative Sequence:** The user is not logged in.
  1. The system redirects the user to the login page.
- **Post Conditions:**
  - The items are displayed on the page to the user.
- **Functional Requirements:**
  - The system has access to the user and purchases databases.
- **Non-Functional Requirements:**
  - The website is stylized.
- **Glossary:**
  - Purchased Item = A product that was purchased by the user.
  - User = Customer who wants to buy one or more items.

## Other

### Meeting Schedule
We have scheduled weekly meetings for Friday at 1pm.

### Team Lead
We have selected Aaron as the team lead.
