from app import myobj, db
from app.forms import DeleteItemForm, RegistrationForm, LoginForm, ViewCategoryForm, forgotPassForm, changePassForm, \
    updateForm, CreateItemForm
from app.models import User, Category, Items, Cart
from flask import flash, redirect, render_template, url_for, request, session
from flask_login import UserMixin, logout_user, LoginManager, login_user, current_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


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
    return render_template('index.html')


@myobj.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@myobj.route('/register', methods=['GET', 'POST'])
def register():
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
    form = forgotPassForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            session['email'] = form.email.data  # session variable that allows for storing of email into a cookie
            return redirect(url_for('changePass'))
        else:
            flash('Invalid email address')
        return redirect(url_for('forgotPass'))
    return render_template('forgot_pass.html', form=form)


@myobj.route('/changePass', methods=['GET', 'POST'])
def changePass():
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
    logout_user()
    return redirect(url_for('index'))


@myobj.route("/delete_user")
@login_required
def delete_user():
    user = current_user
    db.session.delete(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('index'))


@myobj.route("/update_info", methods=['GET', 'POST'])
@login_required
def update_info():
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
    form = DeleteItemForm()
    item = Items.query.get(itemID)
    if (form.validate_on_submit()):
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for("index"))
    category = Category.query.get(item.categoryID).category_name
    seller = User.query.get(item.sellerID)
    return render_template('item.html', item=item, category=category, seller=seller, current_user=current_user,
                           form=form)


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
