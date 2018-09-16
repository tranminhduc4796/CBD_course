from models import User, Item, Bid, db
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
# When delete:
# db.session.delete(User.query.filter_by(username='guest_1').first)

# Step 2: 1 user auction a baseball
# The below line gets an error if we don't delete the prior database.
#########
item_1 = Item(name="baseball", description='ABC', owner=guest_1) # guest_1 auctions item_1
db.session.add(item_1)
db.session.commit()
print(Item.query.all())
#########
# Step 3: 2 user place bids on the baseball
bid1 = Bid(price=100, payer=guest_2, item= item_1)
bid2 = Bid(price=200, payer=guest_3, item= item_1)
db.session.add(bid1)
db.session.add(bid2)
db.session.commit()
print(Bid.query.all())
# Step 4: Find the highest bid on baseball
highest_bid = Bid.query.filter_by(item_id = 1).order_by(Bid.price)[-1]
# Step 5: Update the item_1 with the highest price
item_1.bid = highest_bid
db.session.commit()
print(item_1.bid)