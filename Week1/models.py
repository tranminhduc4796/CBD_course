from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


file_path = os.path.abspath(os.getcwd()) + "/test.db"
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path
db = SQLAlchemy(app)
"""RELATION IN SQL"""
# Many to one: Foreign key only on the many side
# Many to many: 2 Foreign key with an associated table
# One to one: uselist = False

"""INITIALIZE TABLE FOR MANY-MANY RELATIONS"""
# Auction Table: Users auction many items
"""
auction_table = db.Table('auction_table',
                         Column('item_id', Integer, db.ForeignKey(
                             'item.id'), primary_key=True),
                         Column('user_id', Integer, db.ForeignKey(
                             'user.id'), primary_key=True))
# Bid Table: Users bid many items
bid_table = db.Table('bid_table',
                     Column('bid_id', Integer, db.ForeignKey(
                         'bid.id'), primary_key=True),
                     Column('user_id', Integer, db.ForeignKey(
                         'user.id'), primary_key=True))
"""

#Relation in this database#

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    # Configuration for User auction Items (One-Many)
    auction_items = db.relationship('Item', backref='owner')
    # Configuration for Users bid Items
    bids = db.relationship('Bid', backref='payer')

    def __repr__(self):
        return '<User %r with id %r>' % (self.username, self.id)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    # Configuration for User auction Items(One-Many)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # Configuration for Bid-Item
    bid = db.relationship("Bid", uselist=False, backref='item')

    def __repr__(self):
        return '<Item %r owner_id %r>' % (self.name, self.id)


class Bid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    # Configuration for Bid-Item(One-One)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    # item = db.relationship("Item", uselist=False, backref=db.backref("bid", lazy=True))
    # Configuration for User place Bids(One-Many)
    payer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '[Bid price: %r payer_id: %r item_id: %r]' % (self.price, self.payer_id, self.item_id)