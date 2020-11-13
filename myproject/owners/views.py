from flask import Blueprint, render_template, redirect, url_for, flash
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddForm

owners_blueprints = Blueprint('owners', __name__, template_folder='templates/owners')


@owners_blueprints.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        puppy_id = form.puppy_id.data

        new_owner = Owner(name, puppy_id)
        db.session.add(new_owner)
        db.session.commit()

        flash(f'You just added the owner: {name}!')
        return redirect(url_for('puppies.list'))

    return render_template('add_owner.html', form=form)
