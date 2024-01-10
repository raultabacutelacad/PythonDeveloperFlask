from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)

## TODO Actually pull entries out of the db
calendar_entries = {
    1: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 1'},
    2: {'id':2, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 2'},
    3: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 3'},
    4: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 4'},
    5: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 5'},
    6: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 6'},
    7: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 7'},
    8: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 8'},
    9: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 9'},
    10: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 10'},
    11: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 11'},
    12:{'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 12'},
    13: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 13'},
    14: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 14'},
    15: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 15'},
    16: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 16'},
    17: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 17'},
    18: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 18'},
    19: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 19'},
    20: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 20'},
    21: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 21'},
    22: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 22'},
    23: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 23'},
    24: {'id':1, 'imagine': 'img1.jpg', 'mesaj': 'Text pentru ziua 24'},
}


@app.route("/css/<path:file>")
def return_css(file):
    return send_from_directory('css', file)

@app.route('/')
def index():
    list = calendar_entries.values()
    return render_template('index.html', calendar_entries=list)

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
    app.run(debug=True)

    @app.route('/mark_day',methods=['GET', 'POST'])
    def mark_day():
        if request.method == 'POST':
            return "Ziua a fost marcata ca fiind deschisa sau inchisa"
        else:
            return
        render_template('mark_day.html')