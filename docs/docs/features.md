# Features
This is a features documentation for our user guide.

## routes.login()
Allows the user to login after entering their email and password.

#### Parameters
- none

#### Returns
- string: HTML code for webpage to display

## routes.logout()
While a user is logged in, after clicking the logout button, the current user is logged out.
	
#### Parameters
- none

#### Returns
- response object: redirects user to the homepage

## routes.register()
Allows user to register a new account to be stored in the database.
	
#### Parameters
- none

#### Returns
- string :HTML code contained in register.html to display

## routes.delete_user()
displays webpage confirming if the user wants to delete their account
	
#### Parameters
- none

#### Returns
- string: HTML code for webpage to display

## routes.remove_users()
Deletes the user from the database
	
#### Parameters
- none

#### Returns
- response object: redirects to the route for index
	
## routes.update_user()
Renders the update info page which allows the user to change their account information after confirming by
    entering their email
	
#### Parameters
- none

#### Returns
- string: HTML code for webpage to display

## routes.forgot_pass()
Renders the forgot password page which prompts the user to enter their email to find the correct
    security question
	
#### Parameters
- none

#### Returns
 string: HTML code for webpage to display

## routes.change_pass()
Renders the change password page which allows the user to change their password after entering a security
    question
	
#### Parameters
- none

#### Returns
- string: HTML code for webpage to display.

## routes.create_item()
Allows the user to create an item to list on the webstore. Once the item is created, the user is redirected to the item page.

#### Parameters
- none

#### Returns
- string: HTML code for webpage to display.

#### User Description
A user who is logged into their account has the option to list an item they want to sell to our store site. The user clicks on the "Create New Item" link in the upper right hand corner tab of the site. The seller would have to include the following required information: the name of the item, description, price, the number of quantity of a particular item, choose item condition from a dropdown menu, and basic category the item belongs in. Once the user has included the required information, the item will be available for sale and can be viewed in the "All Items" tab.
	
## routes.all_items()
Displays all available items to the user, or only those of a specific category if requested. If the item category is listed as 'all items', then the user is redirected to the all items view.

#### Parameters
- none

#### Returns
- string: HTML code for webpage to display.

#### User Description
Any user who is logged into their account or not logged in at all can view all the available items listed on the entire store site. The user will have to click on the "All items" link at the upper right corner tab and it would lead the user to see all the items on the site for sale.
	
## routes.view_item(itemID)
Displays an individual item to the user.

#### Parameters
- itemID (int): The id for the item to display.

#### Returns
- string: HTML code for webpage to display.

#### User Description
Any user regardless of logged in status or not can also click on an item to view the information about that particular item. The user would have to click on "All Items" to bring up a page that show all the avaialble items and then click on the name of the product in order to view that single item and see any additional information and pictures of the item. <br/><br/>
If the user is the one who is selling the item, the user can click on the particular item they wish to delete a listing of and clicks on "Delete Item" button to delete the item from store.

## routes.addToCart(itemID)
Allows logged in user to add an item to a cart. If a user clicks the same item to add into their cart, the item quantity in the user's cart updates by one. 

#### Parameters:
- itemID (int): id for the item to add to the cart.

#### Returns
- string: HTML code for webpage to display cart information just added.

## routes.view_cart()
Displays a users cart by showing each item individually.

#### Parameters:
- none

#### Returns
- string: HTML code for webpage to display the current user's cart.

## routes.update_item()
Allows a seller to edit their own item. Reuses the create item form, which allows the user to input new values for the item.

#### Parameters:
- itemID (int): id for the item to update.

#### Returns
- string: HTML code for webpage to display that allows seller to update item.

## routes.checkoutCart()
Allows users to buy and checkout items from their cart. 

#### Parameters:
- none

#### Returns
- string: HTML code for webpage to display the checkout page.
