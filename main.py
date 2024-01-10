from flask import Flask, render_template, request, redirect, url_for, send_from_directory
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



calendar_entries = {
    1: {'image': 'img1.jpg', 'text': 'Text pentru ziua 1'},
}

@app.route("/css/<path:file>")
def return_css(file):
    return send_from_directory('css', file)

@app.route('/')
def index():
    return render_template('index.html', calendar_entries=calendar_entries)

@app.route('/edit/<int:day>', methods=['GET', 'POST'])
def edit(day):
    entry = calendar_entries.get(day)
    if request.method == 'POST':
        if 'image' in request.files:
            image_file = request.files['image']
            image_file.save(f"static/{image_file.filename}")
            entry['image'] = f"static/{image_file.filename}"

        entry['text'] = request.form['text']
        return redirect(url_for('index'))
    return render_template('edit.html', day=day, entry=entry)


if __name__ == "__main__":
    #crearea tabelelor si modelelor
    with app.app_context():
        db.create_all()
        print(Ziua.query.all())
    app.run(debug=True)