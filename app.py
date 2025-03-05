from flask import Flask, render_template
from calc import compCompatibility


app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template("pyaar.html")


@app.route('/calc', methods=["POST"])
def calculate():
    # name1 and name2 will take from form
    comp = compCompatibility(name1, name2)


if __name__ == "__main__":
    app.run(debug=True)
