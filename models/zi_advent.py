from flask import Flask, request, redirect, jsonify
from flask import render_template


app = Flask(__name__)

zile = [{'zi': 1}, {'zi': 2}, {'zi': 3}, {'zi': 4}, {'zi': 5}, {'zi': 6}, {'zi': 7}, {'zi': 8},
        {'zi': 9}, {'zi': 10}, {'zi': 11}, {'zi': 12}, {'zi': 13}, {'zi': 14}, {'zi': 15}, {'zi': 16},
        {'zi': 17}, {'zi': 18}, {'zi': 19}, {'zi': 20}, {'zi': 21}, {'zi': 22}, {'zi': 23}, {'zi': 24}]

@app.route("/")
def root_advent():
    return render_template("homepage.html", titlu="Advent Calendar")


@app.route('/editeaza/<int:zi_id>', methods=['GET', 'POST'])
def editeaza_zi(zi_id):
    ziua_x = {}
    for zi in zile:
        if zi['id'] == zi_id:
            zi_x = zi
            break
    return jsonify(ziua_x)

if __name__ == "__main__":
    app.run(debug=True)

