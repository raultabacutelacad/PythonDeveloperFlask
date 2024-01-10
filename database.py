from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/advent'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Ziua(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numar_zi = db.Column(db.Integer)
    imagine = db.Column(db.String(255))
    mesaj = db.Column(db.String(255))
    deschis = db.Column(db.Boolean)
