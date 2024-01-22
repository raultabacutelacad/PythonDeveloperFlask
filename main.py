from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@127.0.0.1:3306/advent'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Ziua(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numar_zi = db.Column(db.Integer)
    imagine = db.Column(db.String(255))
    mesaj = db.Column(db.String(255))
    deschis = db.Column(db.Boolean)

@app.route("/css/<path:file>")
def return_css(file):
    return send_from_directory('css', file)

@app.route('/')
def index():
    zile = Ziua.query.all()
    return render_template('index.html', zile=zile)

@app.route('/deschide/<int:day>')
def deschide(day): 
    zi = Ziua.query.get(day)
    zi.deschis=1
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/inchide/<int:day>")
def inchide(day): 
    zi = Ziua.query.get(day)
    zi.deschis=0
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:day>', methods=['GET', 'POST'])
def edit(day):
    entry = Ziua.query.get(day)
    if request.method == 'POST':
        if 'image' in request.files and request.files['image'].filename:
            image_file = request.files['image']
            image_file.save(f"static/{image_file.filename}")
            entry.imagine = image_file.filename

        entry.mesaj = request.form['text']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', day=day, entry=entry)


if __name__ == "__main__":
    #crearea tabelelor si modelelor
    with app.app_context():
        db.create_all()
        print(Ziua.query.all())
    app.run(debug=True)