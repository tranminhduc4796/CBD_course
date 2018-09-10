from models import *
db.create_all() # Create database
# Step 1: Add 3 users
guest_1 = User(username="guest_1", password="1")
guest_2 = User(username="guest_2", password="2")
guest_3 = User(username="guest_3", password="3")
db.session.add(guest_1)
db.session.add(guest_2)
db.session.add(guest_3)
db.session.commit()
print(User.query.all())
# Step 2: 1 user auction a baseball
item_1 = Item(name="baseball", auction_user=guest_1)
db.session.add(item_1)
print(guest_1.items)
