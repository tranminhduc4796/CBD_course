from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Column, Integer, DateTime, Float
from datetime import datetime
import os


file_path = os.path.abspath(os.getcwd()) + "/test.db"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///' + file_path
db = SQLAlchemy(app)
"""RELATION IN SQL"""
# Many to one: Foreign key only on many side
# Many to many: 2 Foreign key with an associated table
# One to one: uselist = False

"""INITIALIZE TABLE FOR MANY-MANY RELATIONS"""
# Auction Table: Users auction many items
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


class Item(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    start_time = Column(DateTime, default=datetime.utcnow)
    # Configuration for Bid-Item
    bid = db.relationship("Bid", backref=db.backref("item", lazy=True))
    # Configuration for Users auction Items
    auction_user = db.relationship(
        "User", secondary=auction_table, backref=db.backref("items", lazy=True))

    def __repr__(self):
        return '<Item %r>' % self.name


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    # Configuration for Users auction Items
    auction_item = db.relationship(
        "Item", secondary=auction_table, backref=db.backref("users",lazy=True))
    # Configuration for Users bid Items
    bid = db.relationship("Bid", secondary=bid_table, backref=db.backref("users",lazy=True))

    def __repr__(self):
        return '<User %r>' % self.username


class Bid(db.Model):
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    # Configuration for Bid-Item
    item_id = Column(Integer, db.ForeignKey('item.id'))
    item = db.relationship("Item", uselist=False, backref=db.backref("bid", lazy=True))
    # Configuration for Users bid Items
    user = db.relationship("User", secondary=bid_table, backref=db.backref("bids", lazy=True))

    def __repr__(self):
        return '<Bid %r>' % self.price
