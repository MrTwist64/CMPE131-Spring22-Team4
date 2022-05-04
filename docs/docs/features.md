# Features
This is a features documentation for our user guide.

## Login
You can login to our site by clicking on the Login page in the upper right corner. Then type in your email address and password. Click the remember me checkbox if you want the site to remember that you are logged in. After putting in your username, password, and checking the remember me box, then click the submit button to log into your account. 

## Logout
You can logout by clicking the logout button on the top of the tab. 
	
## Create New Account
Users can create a new account in our store site by adding their first name, last name, username, email, and password. It would then create an account in which users have the option to buy and sell items in our store site.

## Delete Account
User can delete their existing account. The user will have to be first logged into their account. Then logged in users can simply click the "Delete Account" link located near the upper right corner of the site under the welcome message to delete their account from our site. 
	
## Update Account
Users can update their information in their account if they so wish. First users would have to click on the "Update Info" link on the top right corner of the page right below the Welcome user message. Then the user will enter a page to update their either first name, last name, username, email, or password. The user will have to confirm their email address again for the system to update account information. Any other information left blank will not be updated.
	
## Forgot Password
If users cannot log in because they forgot their password, then they can create a new password by first typing in their email address. The site will then show the user's security question and prompt the user that matches with the email address to first answer the security question, and then type in their new password. The user will also have to verify that new password. Once the user has added their password twice, the system will update the new password credential for the user.
	
## routes.create_item()
Allows the user to create an item to list on the webstore. Once the item is created, the user is redirected to the item page.

#### Parameters
- none

#### Returns
- string: HTML code for webpage to display

#### User Description
A user who is logged into their account has the option to list an item they want to sell to our store site. The user clicks on the "Create New Item" link in the upper right hand corner tab of the site. The seller would have to include the following required information: the name of the item, description, price, the number of quantity of a particular item, choose item condition from a dropdown menu, and basic category the item belongs in. Once the user has included the required information, the item will be available for sale and can be viewed in the "All Items" tab.
	
## routes.all_items()
Displays all available items to the user, or only those of a specific category if requested. If the item category is listed as 'all items', then the user is redirected to the all items view.

#### Parameters
- none

#### Returns
- string: HTML code for webpage to display

#### User Description
Any user who is logged into their account or not logged in at all can view all the available items listed on the entire store site. The user will have to click on the "All items" link at the upper right corner tab and it would lead the user to see all the items on the site for sale.
	
## routes.view_item(itemID)
Displays an individual item to the user

#### Parameters
- itemID (int): The id for the item to display

#### Returns
- string: HTML code for webpage to display

#### User Description
Any user regardless of logged in status or not can also click on an item to view the information about that particular item. The user would have to click on "All Items" to bring up a page that show all the avaialble items and then click on the name of the product in order to view that single item and see any additional information and pictures of the item. <br/><br/>
If the user is the one who is selling the item, the user can click on the particular item they wish to delete a listing of and clicks on "Delete Item" button to delete the item from store.
