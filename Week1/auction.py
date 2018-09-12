from models import User, Item, Bid, db
db.create_all() # Create database
# Step 1: Add 3 users
guest_1 = User(id=1, username="guest_1", password="1")
guest_2 = User(id=2, username="guest_2", password="2")
guest_3 = User(id=3, username="guest_3", password="3")
db.session.add(guest_1)
db.session.add(guest_2)
db.session.add(guest_3)
db.session.commit()
print(User.query.all())
# When delete:
# db.session.delete(User.query.filter_by(username='guest_1').first)

# Step 2: 1 user auction a baseball
# The below line get an error
#########
item_1 = Item(name="baseball", description='ABC', owner=guest_1)
db.session.add(item_1)
db.session.commit()
print(Item.query.all())
#########
# Step 3: 2 user place bids on the baseball
