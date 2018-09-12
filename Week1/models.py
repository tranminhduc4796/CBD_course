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
# Many to one: Foreign key only on many side
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


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    # Configuration for Users auction Items
    # When add the below line, everything is fucked up (And the line 54 too)
    auction_items = db.relationship('Item', backref='owner')
    # Configuration for Users bid Items
    # bid = db.relationship("Bid", secondary=bid_table, backref=db.backref("users",lazy=True))

    def __repr__(self):
        return '<User %r with id %r>' % (self.username, self.id)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    # Configuration for User auction Items
    # When add the below line, everything is fucked up
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # Configuration for Bid-Item
    # bid = db.relationship("Bid", backref=db.backref("item", lazy=True))

    def __repr__(self):
        return '<Item %r with id %r>' % (self.name, self.id)


class Bid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    # Configuration for Bid-Item
    # item_id = Column(Integer, db.ForeignKey('item.id'))
    # item = db.relationship("Item", uselist=False, backref=db.backref("bid", lazy=True))
    # Configuration for Users bid Items
    # user = db.relationship("User", secondary=bid_table, backref=db.backref("bids", lazy=True))

    def __repr__(self):
        return '<Bid %r>' % self.price
