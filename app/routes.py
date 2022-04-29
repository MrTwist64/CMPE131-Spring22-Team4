from app import myobj, db
from app.models import User, Category, Items, Cart
from flask import flash, redirect, render_template, url_for, request, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from flask_login import UserMixin, logout_user, LoginManager, login_user, current_user
from wtforms.validators import DataRequired, Email, EqualTo
from app.forms import RegistrationForm, LoginForm, forgotPassForm, changePassForm, updateForm

login_manager = LoginManager()
login_manager.init_app(myobj)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


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
            user = User(first_name=form.firstname.data, last_name=form.lastname.data, username=form.username.data, email=form.email.data, securityQuestion=form.securityQuestion.data)
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


@myobj.route('/forgotPass', methods=['GET', 'POST'])
def forgotPass():
    form = forgotPassForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            session['email'] = form.email.data
            form = changePassForm()

            return redirect(url_for('changePass'))
        else:
            flash('Invalid email address')
        return redirect(url_for('forgotPass'))
    return render_template('forgot_pass.html', form=form)


@myobj.route('/changePass', methods=['GET', 'POST'])
def changePass():
    form = changePassForm()
    user = User.query.filter_by(email=session['email']).first()
    if form.validate_on_submit():
        if user.check_security_answer(form.securityQuestionAnswer.data):
            user.set_password(form.password1.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            flash('Invalid answer')
    return render_template('changePass.html', form=form, email=session['email'], securityQuestion=user.securityQuestion)


@myobj.route("/logout")
# @login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@myobj.route("/delete_user")
# @login_required
def delete_user():
    user = current_user
    db.session.delete(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('index'))


@myobj.route("/update_info", methods=['GET', 'POST'])
# @login_required
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
    items = Items.query.all()
    categories = Category.query.all()
    return render_template('all_items.html', items=items, categories=categories)


@myobj.route('/i/<int:itemID>', methods=['GET', 'POST'])
def view_item(itemID):
    item = Items.query.get(itemID)
    category = Category.query.get(item.categoryID).category_name
    seller = User.query.get(item.sellerID).username
    return render_template('item.html', item=item, category=category, seller=seller)
