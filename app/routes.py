from app import myobj, db
from app.forms import DeleteItemForm, RegistrationForm, LoginForm, ViewCategoryForm, forgotPassForm, changePassForm, \
    updateForm, CreateItemForm, CreateCheckoutForm
from app.models import User, Category, Items, Cart
from flask import flash, redirect, render_template, url_for, request, session
from flask_login import UserMixin, logout_user, LoginManager, login_user, current_user, login_required
from flask_wtf import FlaskForm
from flask_session import Session
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo
from sqlalchemy.exc import IntegrityError
from sqlalchemy import and_


login_manager = LoginManager()
login_manager.init_app(myobj)


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


# -------------------- Routes --------------------
@myobj.route('/', methods=['GET', 'POST'])
@myobj.route('/index', methods=['GET', 'POST'])
def index():
    """ Renders the home index page

    Parameters
    -------------------
    none

    Returns
    -------------------
    string
        HTML code contained in webpage to display
    """
    return render_template('index.html')


@myobj.route('/register', methods=['GET', 'POST'])
def register():
    """ Renders the register page which prompts for first name, last name, email, password, security question, and
    security answer

    Parameters
    -------------------
    None

    Returns
    -------------------
    string
        HTML code contained in register.html to display
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        if db.session.query(db.exists().where(User.email == form.email.data)).scalar():
            flash('Email already registered')
        elif db.session.query(db.exists().where(User.username == form.username.data)).scalar():
            flash('Username already registered')
        else:
            user = User(first_name=form.firstname.data, last_name=form.lastname.data, username=form.username.data,
                        email=form.email.data, securityQuestion=form.securityQuestion.data)
            user.set_password(form.password1.data)
            user.set_security_answer(form.securityQuestionAnswer.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register.html', form=form)


@myobj.route('/login', methods=['GET', 'POST'])
def login():
    """ Renders the login page which prompts for email and password

    Parameters
    -------------------
    None

    Returns
    -------------------
    string
        HTML code contained in login.html to display
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            return redirect(next or url_for('index'))
        flash('Invalid email address or Password.')
    return render_template('login.html', form=form)


# Used to validate email before allowing the user to change and printing their security question
@myobj.route('/forgotPass', methods=['GET', 'POST'])
def forgot_pass():
    """ Renders the forgot password page which prompts the user to enter their email to find the correct
    security question

    Parameters
    -------------------
    None

    Returns
    -------------------
    string
        HTML code contained in forgot_pass.html to display
    """
    form = forgotPassForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            session['email'] = form.email.data  # session variable that allows for storing of email into a cookie
            return redirect(url_for('changePass'))
        else:
            flash('Invalid email address')
        return redirect(url_for('forgot_pass'))
    return render_template('forgot_pass.html', form=form)


@myobj.route('/changePass', methods=['GET', 'POST'])
def changePass():
    """ Renders the change password page which allows the user to change their password after entering a security
    question

    Parameters
    -------------------
    None

    Returns
    -------------------
    string
        HTML code contained in change_pass.html to display
    """
    form = changePassForm()
    user = User.query.filter_by(email=session['email']).first()  # uses session variable from forgotPass to verify
    if form.validate_on_submit():
        if user.check_security_answer(form.securityQuestionAnswer.data):
            user.set_password(form.password1.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            flash('Invalid answer')
    return render_template('change_pass.html', form=form, email=session['email'],
                           securityQuestion=user.securityQuestion)


@myobj.route("/logout")
@login_required
def logout():
    """ Logs out the current user

    Parameters
    -------------------
    None

    Returns
    -------------------
    response object
        redirects to the route for index
    """
    logout_user()
    return redirect(url_for('index'))


@myobj.route("/delete_user")
@login_required
def delete_user():
    """ Deletes the current user

        Parameters
        -------------------
        None

        Returns
        -------------------
        response object
            redirects to the route for index
        """
    return render_template('delete_user.html')


@myobj.route("/remove_user")
@login_required
def remove_user():
    """ Deletes the current user

    Parameters
    -------------------
    None

    Returns
    -------------------
    response object
        redirects to the route for index
    """
    user = current_user
    db.session.delete(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('index'))


@myobj.route("/update_info", methods=['GET', 'POST'])
@login_required
def update_info():
    """ Renders the update info page which allows the user to change their account information after confirming by
    entering their email

    Parameters
    -------------------
    None

    Returns
    -------------------
    string
        HTML code contained in update_info.html to display
    """
    form = updateForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=current_user.email).first()
        if request.form.get('username', None):
            user.username = form.username.data
        if request.form.get('firstname', None):
            user.first_name = form.firstname.data
        if request.form.get('lastname', None):
            user.last_name = form.lastname.data
        if request.form.get('password1', None) and request.form.get('password2', None):
            user.set_password(form.password1.data)
        if request.form.get('email', None):
            user.email = form.email.data
        if request.form.get('securityQuestion', None):
            user.securityQuestion = form.securityQuestion.data
        if request.form.get('securityQuestionAnswer', None):
            user.set_security_answer(form.securityQuestionAnswer.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template('update_info.html', form=form)


@myobj.route('/all_items', methods=['GET', 'POST'])
def all_items():
    """ Displays all available items to the user, or only those of a specific category if requested.
    If the item category is listed as 'all items', then the user is redirected to the all items view.

    Parameters
    -------------------
    none

    Returns
    -------------------
    string
        HTML code for webpage to display
    """
    form = ViewCategoryForm()
    categories = Category.query.all()
    requested_category = request.args.get('category')
    if (requested_category):
        if (requested_category == '18'): # The category for viewing all items
            return redirect(url_for('all_items'))
        items = Items.query.filter(Items.categoryID == int(requested_category))
        return render_template('all_items.html', items=items, categories=categories, form=form, 
                               selected_category=int(requested_category))
    items = Items.query.all()
    return render_template('all_items.html', items=items, categories=categories, form=form)


@myobj.route('/i/<int:itemID>', methods=['GET', 'POST'])
def view_item(itemID):
    """ Displays an individual item to the user

    Parameters
    -------------------
    itemID: int
        The id for the item to display

    Returns
    -------------------
    string
        HTML code for webpage to display
    """
    delete_form = DeleteItemForm()
    item = Items.query.get(itemID)
    if (delete_form.validate_on_submit()):
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for("index"))
    category = Category.query.get(item.categoryID).category_name
    seller = User.query.get(item.sellerID)
    return render_template('item.html', item=item, category=category, seller=seller, current_user=current_user,
                           delete_form=delete_form)


@myobj.route('/create_item', methods=['GET', 'POST'])
@login_required
def create_item():
    """ Allows the user to create an item to list on the webstore. 
    Once the item is created, the user is redirected to the item page.

    Parameters
    -------------------
    none

    Returns
    -------------------
    string
        HTML code for webpage to display
    """
    form = CreateItemForm()
    if (form.validate_on_submit()):
        item = Items()
        item.product_name = form.product_name.data
        item.description = form.description.data
        item.price = form.price.data
        item.quantity = form.quantity.data
        item.condition = form.condition.data
        item.categoryID = form.category.data
        item.sellerID = current_user.id
        db.session.add(item)
        db.session.commit()
        return redirect(f'/i/{item.itemID}')
    return render_template('create_item.html', form=form)
    
    
@myobj.route('/i/<int:itemID>/cart', methods=['GET', 'POST'])
def addToCart(itemID):
    """ Allows the user whether they are logged in or not to add an item to their cart.

    Parameters
    -------------------
    itemID: int
        The id for the item to add to the cart

    Returns
    -------------------
    string
        HTML code for webpage to display
    """
    
    # the user is already logged into their account
    if (current_user.is_authenticated):
        user = current_user
    # the user is not logged in, and will continue as guest
    elif (current_user.is_anonymous):
        user = User.query.filter_by(first_name="Guest").first()   
    else:    
        return redirect(f'/i/{item.itemID}')
        
    item = Items.query.get(itemID)
    
    try:
        # default quantity added to cart is one item
        cart = Cart(userID = user.id, itemID = itemID, quantity= 1)
        db.session.add(cart)
        db.session.commit()
    # Unique constraint error when user adds same item in cart
    # Updates existing cart item by adding quantity by one when 'add to cart' is pressed again
    except IntegrityError:
        db.session.rollback()
        flash("You have already added this item into your cart.")
        cartQuery = Cart.query.filter((Cart.userID == user.id) & (Cart.itemID == itemID)).first()
        # Prevents adding more items to cart than are available to buy
        if (cartQuery.quantity < item.quantity):
            cartQuery.quantity = cartQuery.quantity + 1
        db.session.commit()
    return redirect(url_for('view_cart'))
    

@myobj.route('/cart', methods=['GET', 'POST'])
@login_required
def view_cart():
    """ Displays a users cart by showing each item individually.

    Parameters
    -------------------
    none

    Returns
    -------------------
    string
        HTML code for webpage to display
    """
    cartItems = Cart.query.filter(Cart.userID == current_user.id)
    items = []
    subtotal = 0
    for cartItem in cartItems:
        item = Items.query.get(cartItem.itemID)
        items.append(item)
        subtotal += item.price * cartItem.quantity
    return render_template('view_cart.html', currentUser=current_user, cartItems=cartItems, items=items, subtotal=subtotal)


@myobj.route('/i/<int:itemID>/update', methods=['GET', 'POST'])
def update_item(itemID):
    """ Allows a seller to edit their own item.

    Parameters
    -------------------
    itemID: int
        The id for the item to update

    Returns
    -------------------
    string
        HTML code for webpage to display
    """
    item = Items.query.get(itemID)
    if (current_user.id != item.sellerID):
        return redirect('/i/itemID')
    form = CreateItemForm()
    if (form.validate_on_submit()):
        item.product_name = form.product_name.data
        item.description = form.description.data
        item.price = form.price.data
        item.quantity = form.quantity.data
        item.condition = form.condition.data
        item.categoryID = form.category.data
        db.session.add(item)
        db.session.commit()
        return redirect(f'/i/{item.itemID}')
    return render_template('update_item.html', item=item, form=form)

@myobj.route('/cart/<int:cartID>/remove', methods=['GET', 'POST'])
def removeItemFromCart(cartID):
    """ Allows users to remove an item from their cart

    Parameters
    -------------------
    itemID: int
        The id for the cart row for the item needed to removed from the cart

    Returns
    -------------------
    string
        HTML code for webpage to display
    """
    cartToDelete = Cart.query.get(cartID)
    db.session.delete(cartToDelete)
    db.session.commit()
    
    return redirect(url_for('view_cart'))

@myobj.route('/checkout', methods=['GET', 'POST'])
def checkoutCart():
    """ Allows users to checkout their cart

    Parameters
    -------------------
    none

    Returns
    -------------------
    string
        HTML code for webpage to display
    """

    form = CreateCheckoutForm()
    if (form.validate_on_submit()):
        cartItems = Cart.query.filter(Cart.userID == current_user.id)
        for item in cartItems:
            
            db.session.delete(item)
        db.session.commit()
        return redirect(url_for('view_cart'))
        
    # shipping info
    address = form.address.data
    # credit card info
    creditCardNum = form.payment.data
    cvv = form.cvv.data
    return render_template('checkout.html', form=form)

