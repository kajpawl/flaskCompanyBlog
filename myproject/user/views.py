from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash
from myproject import db
from myproject.models import User
from myproject.user.forms import RegisterForm, LoginForm, EditForm
from flask_login import login_user, login_required, logout_user

user_blueprints = Blueprint('user', __name__, template_folder='templates/user')


@user_blueprints.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(name=form.name.data,
                        surname=form.surname.data,
                        email=form.email.data,
                        password=form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash('User registered!')
        return redirect(url_for('user.login'))

    return render_template('register.html', form=form)


@user_blueprints.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!')

            next = request.args.get('next')
            if next is None or not next[0] == '/':
                next = url_for('puppies.list')

            return redirect(next)
        else:
            flash('Login attempt failed.')

    return render_template('login.html', form=form)


@user_blueprints.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.check_password(form.password.data):
            user.name = form.name.data
            user.surname = form.surname.data
            user.email = form.email.data
            user.password_hash = generate_password_hash(form.new_password.data)

            db.session.add(user)
            db.session.commit()

            flash('Account updated!')
        else:
            flash('Invalid password.')

    return render_template('edit.html', form=form)


@user_blueprints.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('index'))
