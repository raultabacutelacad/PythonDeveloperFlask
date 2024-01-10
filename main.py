from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from database import db, Ziua

app = Flask(__name__)


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
    db.create_all()
    app.run(debug=True)