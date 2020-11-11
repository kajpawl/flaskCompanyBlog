# CREATE ENTRIES INTO THE TABLES
from models import db, Puppy, Owner, Toy

# Create 2 puppies
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# ADD PUPPIES TO DB
db.session.add_all([rufus, fido])

# CHECK!
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# CREATE OWNER OBJECT
rufus_owner = Owner('Rufus Owner\'s Name', rufus.id)

# CREATE TOYS
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([rufus_owner, toy1, toy2])
db.session.commit()

# GRAB RUFUS AFTER THOSE ADDITIONS
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
rufus.report_toys()
