from basic import db, Puppy

# Creates all tables: Model --> Db Table
db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)

# None
# None
print(sam.id)
print(frank.id)

db.session.add_all([sam, frank])

db.session.commit()

# 1
# 2
print(sam.id)
print(frank.id)
