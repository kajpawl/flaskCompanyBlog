from myproject import db


class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name: {self.name}, owner: {self.owner.name}"
        else:
            return f"Puppy name: {self.name}, it has no owner yet!"


class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner name: {self.name}, puppy id: {self.puppy_id}."


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    surname = db.Column(db.Text)
    email = db.Column(db.Text)
    password_hash = db.Column(db.Text)

    def __init__(self, name, surname, email, password_hash):
        self.name = name
        self.surname = surname
        self.email = email
        self.password_hash = password_hash

    def __repr__(self):
        return f"{self.name} {self.surname}: {self.email}"
