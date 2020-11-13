from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from myproject import db
from myproject.models import User
from myproject.user.forms import RegisterForm, LoginForm, EditForm

user_blueprints = Blueprint('user', __name__, template_folder='templates/user')


@user_blueprints.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password_hash = generate_password_hash(form.password.data)

        new_user = User(name, surname, email, password_hash)
        db.session.add(new_user)
        db.session.commit()

        flash('User registered!')
        return redirect(url_for('puppies.list'))

    return render_template('register.html', form=form)


@user_blueprints.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        correct_password = check_password_hash(user.password_hash, form.password.data)

        if user is not None and correct_password is True:
            flash('Login successful!')
            return redirect(url_for('puppies.list'))
        else:
            flash('Login attempt failed.')

    return render_template('login.html', form=form)


@user_blueprints.route('/edit', methods=['GET', 'POST'])
def edit():
    form = EditForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        correct_password = check_password_hash(user.password_hash, form.password.data)

        if user is not None and correct_password is True:
            user.name = form.name.data
            user.surname = form.surname.data
            user.email = form.email.data
            user.password_hash = generate_password_hash(form.new_password.data)

            db.session.add(user)
            db.session.commit()

            flash('Account updated!!')
        else:
            flash('Invalid password.')

    return render_template('edit.html', form=form)


@user_blueprints.route('/logout', methods=['POST'])
def logout():
    return render_template('index.html')

