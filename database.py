from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean

app = Flask(__name__)
db = SQLAlchemy(app)

class Ziua(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numar_zi = db.Column(db.Integer)
    imagine = db.Column(db.String(255))
    mesaj = db.Column(db.String(255))
    deschis = db.Column(db.Boolean)